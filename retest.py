import re

regex = r'\s*(авто|avto)\s*\:\s*([^,]+?)\s*\,\s*([^,]+?)\s*\,\s*([^,]+?)\s*\,\s*([^,]+?)\s*\,\s*([^,]+?)\s*\,\s*([^,]+?)?$'
# regex = r"\s*(avto|авто)\s*\:\s*(?P<name>[^,]+?)\s*\,\s*(?P<year>[^,]+?)\s*\,\s*(?P<mileage>[^,]+?)\s*\,\s*(?P<status>[^,]+?)\s*\,\s*(?P<price>[^,]+?)\s*\,\s*(?P<contact>[^,]+?)?$"

test_str = "авто: нексия донс, 2010, 122 минг юрган  , яхши краскаси йук, 5400 kami bor, юсел 1234567"


# m = re.search(regex, test_str)
# print('Name ->', m.group('name'))
# print('Year ->', m.group('year'))
# print('Mileage ->', m.group('mileage'))
# print('Status ->', m.group('status'))
# print('Price ->', m.group('price'))
# print('Contact ->', m.group('contact'))

matches = re.finditer(regex, test_str)


for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1

    print("Match {matchNum} was found at {start}-{end}: {match}".format(
        matchNum=matchNum, start=match.start(), end=match.end(), match=match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print(
            "Group {groupNum} found at {start}-{end}: {group}".format(
                groupNum=groupNum,
                start=match.start(groupNum),
                end=match.end(groupNum),
                group=match.group(groupNum)))
