from ..gbifutils import *

def name_backbone(name, rank=None, kingdom=None, phylum=None, clazz=None,
  order=None, family=None, genus=None, strict=False, verbose=False,
  start=None, limit=100, **kwargs):
  '''
  Lookup names in the GBIF backbone taxonomy.

  :param name: [str] Full scientific name potentially with authorship (required)
  :param rank: [str] The rank given as our rank enum. (optional)
  :param kingdom: [str] If provided default matching will also try to match against this
     if no direct match is found for the name alone. (optional)
  :param phylum: [str] If provided default matching will also try to match against this
     if no direct match is found for the name alone. (optional)
  :param class: [str] If provided default matching will also try to match against this
     if no direct match is found for the name alone. (optional)
  :param order: [str] If provided default matching will also try to match against this
     if no direct match is found for the name alone. (optional)
  :param family: [str] If provided default matching will also try to match against this
     if no direct match is found for the name alone. (optional)
  :param genus: [str] If provided default matching will also try to match against this
     if no direct match is found for the name alone. (optional)
  :param strict: [bool] If True it (fuzzy) matches only the given name, but never a
     taxon in the upper classification (optional)
  :param verbose: [bool] If True show alternative matches considered which had been rejected.

  A list for a single taxon with many slots (with ``verbose=False`` - default), or a
  list of length two, first element for the suggested taxon match, and a data.frame
  with alternative name suggestions resulting from fuzzy matching (with ``verbose=True``).

  If you don't get a match GBIF gives back a list of length 3 with slots synonym,
  confidence, and ``matchType='NONE'``.

  reference: http://www.gbif.org/developer/species#searching

  Usage::

      from pygbif import species
      species.name_backbone(name='Helianthus annuus', kingdom='plants')
      species.name_backbone(name='Helianthus', rank='genus', kingdom='plants')
      species.name_backbone(name='Poa', rank='genus', family='Poaceae')

      # Verbose - gives back alternatives
      species.name_backbone(name='Helianthus annuus', kingdom='plants', verbose=True)

      # Strictness
      species.name_backbone(name='Poa', kingdom='plants', verbose=True, strict=False)
      species.name_backbone(name='Helianthus annuus', kingdom='plants', verbose=True, strict=True)

      # Non-existent name
      species.name_backbone(name='Aso')

      # Multiple equal matches
      species.name_backbone(name='Oenante')
  '''
  url = gbif_baseurl + 'species/match'
  args = {'name': name, 'rank': rank, 'kingdom': kingdom, 'phylum': phylum,
         'class': clazz, 'order': order, 'family': family, 'genus': genus,
         'strict': strict, 'verbose': verbose, 'offset': start, 'limit': limit}
  tt = gbif_GET(url, args, **kwargs)
  return tt