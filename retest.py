import re

regex = r"\s*.*(?P<auto>[aA][vV][tT][oO]|[аА][вВ][тТ][оО]).*\s*\:\s*(?P<name>[^,]+?)\s*\,\s*(?P<year>[^,]+?)\s*\,\s*(?P<mileage>[^,]+?)\s*\,\s*(?P<status>[^,]+?)\s*\,\s*(?P<contact>[^,]+?)?$"

test_str = "АвТо: нексия донс, 2010, 122 минг юрган  , яхши краскаси йук, юсел 1234567"

matches = re.finditer(regex, test_str)

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
