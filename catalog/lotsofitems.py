from pdb import set_trace as st

from capp.models import lots_of_items
# although this import is unused, it must be included to avoid errors
# when initializing Item objects b/c of the foreign key relation
from cauth.models import User

lots_of_items()
