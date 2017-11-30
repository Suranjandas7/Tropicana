def render_to_main(data):
    title = data[0]
    desc = data[1]
    dictionary = data[2]

    print """
        {}
        =======
    """.format(title)
    print """
        {}
    """.format(desc)

    for d in dictionary:
        print """
            {} : {}""".format(d, dictionary[d])

def convert_to_float(data):
    for d in data:
        try:
            d = float(data)
        except TypeError:
            pass
    print 'MSG : DATA CONVERTED'
    return data
