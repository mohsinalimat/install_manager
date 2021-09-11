import frappe

# http://phaster.com/zip_code.html
POSTAL_CODES = [
    ['AL', 'Huntsville', '35801', '35816'],
    ['AK', 'Anchorage', '99501', '99524'],
    ['AZ', 'Phoenix', '85001', '85055'],
    ['AR', 'Little Rock', '72201', '72217'],
    ['CA', 'Sacramento', '94203', '94209'],
    ['CA', 'Los Angeles', '90001', '90089'],
    ['CA', 'Beverly Hills', '90209', '90213'],
    ['CO', 'Denver', '80201', '80239'],
    ['CT', 'Hartford', '06101', '06112'],
    ['DE', 'Dover', '19901', '19905'],
    ['DC', 'Washington', '20001', '20020'],
    ['FL', 'Pensacola', '32501', '32509'],
    ['FL', 'Miami', '33124', '33190'],
    ['FL', 'Orlando', '32801', '32837'],
    ['GA', 'Atlanta', '30301', '30381'],
    ['HI', 'Honolulu', '96801', '96830'],
    ['ID', 'Montpelier', '83254', '83254'],
    ['IL', 'Chicago', '60601', '60641'],
    ['IL', 'Springfield', '62701', '62709'],
    ['IN', 'Indianapolis', '46201', '46209'],
    ['IA', 'Davenport', '52801', '52809'],
    ['IA', 'Des Moines', '50301', '50323'],
    ['KS', 'Wichita', '67201', '67221'],
    ['KY', 'Hazard', '41701', '41702'],
    ['LA', 'New Orleans', '70112', '70119'],
    ['ME', 'Freeport', '04032', '04034'],
    ['MD', 'Baltimore', '21201', '21237'],
    ['MA', 'Boston', '02101', '02137'],
    ['MI', 'Coldwater', '49036', '49036'],
    ['MI', 'Gaylord', '49734', '49735'],
    ['MN', 'Duluth', '55801', '55808'],
    ['MS', 'Biloxi', '39530', '39535'],
    ['MO', 'St. Louis', '63101', '63141'],
    ['MT', 'Laurel', '59044', '59044'],
    ['NE', 'Hastings', '68901', '68902'],
    ['NV', 'Reno', '89501', '89513'],
    ['NH', 'Ashland', '03217', '03217'],
    ['NJ', 'Livingston', '07039', '07039'],
    ['NM', 'Santa Fe', '87500', '87506'],
    ['NY', 'New York', '10001', '10048'],
    ['NC', 'Oxford', '27565', '27565'],
    ['ND', 'Walhalla', '58282', '58282'],
    ['OH', 'Cleveland', '44101', '44179'],
    ['OK', 'Tulsa', '74101', '74110'],
    ['OR', 'Portland', '97201', '97225'],
    ['PA', 'Pittsburgh', '15201', '15244'],
    ['RI', 'Newport', '02840', '02841'],
    ['SC', 'Camden', '29020', '29020'],
    ['SD', 'Aberdeen', '57401', '57402'],
    ['TN', 'Nashville', '37201', '37222'],
    ['TX', 'Austin', '78701', '78705'],
    ['UT', 'Logan', '84321', '84323'],
    ['VT', 'Killington', '05751', '05751'],
    ['VA', 'Altavista', '24517', '24517'],
    ['WA', 'Bellevue', '98004', '98009'],
    ['WV', 'Beaver', '25813', '25813'],
    ['WI', 'Milwaukee', '53201', '53228'],
    ['WY', 'Pinedale', '82941', '82941'],
]