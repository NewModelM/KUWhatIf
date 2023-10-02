"""
Classes with issues:
- line 53: 3D modeling and Rendering
Fixes:
([^.]*): Attempt at matching the description
(\d{1,3}): Fixed course number issue
"""

from PyPDF2 import PdfReader
import csv
import re
import sys
from pprint import pprint

semester_re = re.compile("(Spring|Summer|Fall|Winter) (\d\d\d\d)")
type_re = re.compile("(Unofficial[a-zA-Z0-9 ]*)")
name_re = re.compile("(Name:)([\S ]*)")
id_re = re.compile("(Student ID:)([a-zA-Z0-9 ]*)")
course_re = re.compile(
    "([A-Z][A-Z][A-Z])[\s\n]*(\d{1,3})([^.]*)(\d\.\d+)[\s\n]*([\d\.\d+]*)[ \n]*(A|A-|B\+|B|B-|CR|C\+|C|D|F|FN|FA|P|PA|S|U|NG|NC|W|M|I|CR)?\n"
)


def strip_qualifiers(text):
    t = text
    result = []
    q_re = re.compile("(WI|VL|CP|CD|CT|CM)")
    m = q_re.match(t)
    while m:
        result.append(m.groups()[0])
        t = t[m.end() :]
        m = q_re.match(t)
    return t, sorted(result)


def munch(text):
    semester_m = semester_re.search(text)
    type_m = type_re.search(text)
    course_m = course_re.search(text)
    index = len(text)
    my_m = None
    for m in [semester_m, type_m, course_m]:
        if not m:
            continue
        if m.start() < index:
            my_m = m
            index = m.start()
    if my_m == None:
        return (None, text)
    else:
        return (my_m, text[my_m.end() :])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit("Usage: <transcript PDF>")

    reader = PdfReader(sys.argv[1])
    chunks = []
    name = None
    student_id = None
    all_text = []
    all_text = ""
    for page in reader.pages:
        all_text += page.extract_text()
    pprint(all_text)
    rows = []
    context = [None, None]
    m, t = munch(all_text)
    while m:
        if len(m.groups()) == 1:
            if "Undergraduate" in m.groups()[0]:
                context = (context[0], "U")
            if "Graduate" in m.groups()[0]:
                context = (context[0], "G")
        if len(m.groups()) == 2:
            context = (" ".join(m.groups()), context[1])
        if len(m.groups()) > 2:
            course_info = m.groups()
            desc = course_info[2].replace("\n", "")
            desc, qual = strip_qualifiers(desc)
            row = [
                course_info[0],
                course_info[1],
                desc,
                ":".join(qual),
                course_info[3] if course_info[4] == "" else course_info[4],
                course_info[5] if course_info[5] else "IP",
                context[0],
                context[1],
            ]
            rows.append(row)
        m, t = munch(t)

    name_tok = name_re.search(all_text)
    name = name_tok.groups()[1].strip()

    id_tok = id_re.search(all_text)
    id = id_tok.groups()[1].strip()

    filename = "-".join(name.split() + [id]) + ".csv"

    with open(filename, mode="w") as f:
        writer = csv.writer(f, delimiter=",", quotechar='"')
        writer.writerow(
            [
                "ID",
                "Student",
                "Department",
                "Number",
                "Name",
                "Qualifiers",
                "Earned",
                "Grade",
                "Semester",
                "Type",
            ]
        )
        for row in rows:
            row = [id, name] + row
            writer.writerow(row)
