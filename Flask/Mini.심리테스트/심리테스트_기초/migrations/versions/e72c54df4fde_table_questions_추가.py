"""table: questions 추가

Revision ID: e72c54df4fde
Revises: c949efa4504c
Create Date: 2024-08-02 18:47:57.164981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e72c54df4fde'
down_revision = 'c949efa4504c'
branch_labels = None
depends_on = None


def upgrade():
    # Check if 'questions' table exists
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    if 'questions' not in inspector.get_table_names():
        op.create_table('questions',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('title', sa.String(length=200), nullable=False),
            sa.PrimaryKeyConstraint('id')
        )

    with op.batch_alter_table('answers', schema=None) as batch_op:
        batch_op.alter_column('participant_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('chosen_answer',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.String(length=20),
               existing_nullable=True)
        batch_op.create_foreign_key('fk_answers_question_id', 'questions', ['question_id'], ['id'])

def downgrade():
    with op.batch_alter_table('answers', schema=None) as batch_op:
        batch_op.drop_constraint('fk_answers_question_id', type_='foreignkey')
        batch_op.alter_column('chosen_answer',
               existing_type=sa.String(length=20),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)
        batch_op.alter_column('participant_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # Drop the 'questions' table only if it exists
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    if 'questions' in inspector.get_table_names():
        op.drop_table('questions')
