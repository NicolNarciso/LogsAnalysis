#!/usr/bin/env python3

import psycopg2


def report1(cursor):
    result = ''
    result += '1. What are the most popular three articles of all time?\n'
    result += '   Which articles have been accessed the most?\n'
    result += '   Present this information as a sorted list\n'
    result += '   with the most popular article at the top.\n'
    cursor.execute(('SELECT title, count(*) as views FROM articles '
                    'JOIN log '
                    'ON articles.slug = substring(log.path, 10) '
                    'GROUP BY title '
                    'ORDER BY views DESC '
                    'LIMIT 3;'))
    for idx, item in enumerate(cursor.fetchall()):
        result += '      {}. {:35} {}views\n'.format(idx+1, item[0], item[1])
    result += '\n'
    print(result)
    return result


def report2(cursor):
    result = ''
    result += '2. Who are the most popular article authors of all time?\n'
    result += '   That is, when you sum up all of the articles each author\n'
    result += '   has written, which authors get the most page views?\n'
    result += '   Present this as a sorted list with the most popular author\n'
    result += '   at the top.\n'
    cursor.execute(('SELECT authors.name, count(log.id) as views '
                    'FROM authors, articles, log '
                    'WHERE articles.author = authors.id '
                    'AND log.path LIKE \'%\' || articles.slug || \'%\' '
                    'GROUP BY authors.name '
                    'ORDER BY views DESC '
                    'LIMIT 3;'))
    for idx, item in enumerate(cursor.fetchall()):
        result += '      {}. {:35} {}views\n'.format(idx+1, item[0], item[1])
    result += '\n'
    print(result)
    return result


def report3(cursor):
    result = ''
    result += '3. On which days did more than 1% of requests lead to errors?\n'
    result += '   The log table includes a column status that indicates'
    result += ' the HTTP\n'
    result += '   status code that the news site sent to the user\'s'
    result += ' browser.\n'
    cursor.execute(('SELECT to_char(time,\'DD-MON-YYYY\') as day, '
                    'count(*) as count_errors '
                    'FROM log '
                    'WHERE STATUS = \'404 NOT FOUND\' '
                    'GROUP BY day '
                    'ORDER BY count_errors DESC '
                    'LIMIT 1;'))
    for idx, item in enumerate(cursor.fetchall()):
        result += '      {}. {:35} {}errors\n'.format(idx+1, item[0], item[1])
    result += '\n'
    print(result)
    return result


if __name__ == '__main__':
    db_connection = psycopg2.connect(database='news')
    db_cursor = db_connection.cursor()
    with open('result.txt', 'w') as resultfile:
        resultfile.writelines(report1(cursor=db_cursor))
        resultfile.writelines(report2(cursor=db_cursor))
        resultfile.writelines(report3(cursor=db_cursor))
    db_connection.close()
