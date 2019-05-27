#!/usr/bin/env python3

import psycopg2


def report1(cursor):
    result = ''
    result += '1. What are the most popular three articles of all time?\n'
    result += '   Which articles have been accessed the most?\n'
    result += '   Present this information as a sorted list\n'
    result += '   with the most popular article at the top.\n'
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
    result += '\n'

    print(result)
    return result

def report3(cursor):
    result = ''
    result += '3. On which days did more than 1% of requests lead to errors?\n'
    result += '   The log table includes a column status that indicates the HTTP\n'
    result += '   status code that the news site sent to the user\'s browser.\n'
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