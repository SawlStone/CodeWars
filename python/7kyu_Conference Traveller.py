def conference_picker(cities_visited, cities_offered):
    if not cities_visited:   return cities_offered[0]
    try:                     return [i for i in cities_offered if i not in cities_visited][0]
    except Exception:        return 'No worthwhile conferences this year!'


# def conference_picker(cities_visited, cities_offered):
#     if not cities_visited:
#         return cities_offered[0]
#     for of in cities_offered:
#         if of not in cities_visited:
#             return of
#     return 'No worthwhile conferences this year!'


# Test.assert_equals(conference_picker([],['Philadelphia','Osaka','Tokyo','Melbourne']),'Philadelphia','Should work if no cities visited')
# Test.assert_equals(conference_picker([],['Brussels','Madrid','London']),'Brussels','Should work if no cities visited')
# Test.assert_equals(conference_picker([],['Sydney','Tokyo']),'Sydney','Should work if no cities visited')
# Test.assert_equals(conference_picker(['London','Berlin','Mexico City','Melbourne','Buenos Aires','Hong Kong','Madrid','Paris'],['Berlin','Melbourne']),'No worthwhile conferences this year!','Should work if all offered cities previously visited')
# Test.assert_equals(conference_picker(['Beijing','Johannesburg','Sydney','Philadelphia','Hong Kong','Stockholm','Chicago','Seoul','Mexico City','Berlin'],['Stockholm','Berlin','Chicago']),'No worthwhile conferences this year!','Should work if all offered cities previously visited')
# Test.assert_equals(conference_picker(['Mexico City','Dubai','Philadelphia','Madrid','Houston','Chicago','Delhi','Seoul','Mumbai','Lisbon','Hong Kong','Brisbane','Stockholm','Tokyo','San Francisco','Rio De Janeiro'],['Lisbon','Mexico City']),'No worthwhile conferences this year!','Should work if all offered cities previously visited')