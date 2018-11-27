from Bio import Entrez

# Helper function
def _number_by_year(query, year):
    handle = Entrez.esearch(db='pubmed', retmax='200000000', retmode='xml', term=query+" "+str(year)+"[pdat]")
    results = Entrez.read(handle)
    return len(results["IdList"])

# Track absolute number of occurences of a keyword over the years.
def track_absolute(query, year_min=1970, year_max=2018):
    years = [x for x in range(year_min,year_max+1)]
    results = []
    for year in years:
        nb_entries_query = _number_by_year(query, year)
        results.append(nb_entries_query)
    return (years, results)

# Track relative number of occurences of a keyword over the years, compared to the number of all NCBI entries of the respective year.
def track_relative(query, year_min=1970, year_max=2018):
    years = [x for x in range(year_min,year_max+1)]
    results = []
    for year in years:
        nb_entries_query = _number_by_year(query, year)
        nb_all_entries = _number_by_year(" ", year)
        results.append(nb_entries_query/(1.0*nb_all_entries))
    return (years, results)

# Track relative number of occurences of a keyword over the years, compared to the number of occurences of a 'baseline' keyword.
def track_vs_baseline(query, baseline, year_min=1970, year_max=2018):
    years = [x for x in range(year_min,year_max+1)]
    results = []
    for year in years:
        nb_entries_query = _number_by_year(query, year)
        nb_entries_baseline = _number_by_year(baseline, year)
        results.append(nb_entries_query/(1.0*nb_entries_baseline))
    return (years, results)

