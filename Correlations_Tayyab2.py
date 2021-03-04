
#Function for analyzing study programs of bachelor students according to gender
## logic of the function is same as previously used function. Just the variables and type of graph are changed

def geschlecht(x):
    a = df_bachelor['Geschlecht'] == x
    df_bachelor_tmp = df_bachelor[a]
    baselist = df_bachelor_tmp['bachelor_study'].tolist()
    words = frozenset(baselist)
    print (words)
    counted_words = []
    cw= []
    cn= []
    for word in words:
        counted_words.append((word, baselist.count(word)))
        cw.append(word)
        cn.append(baselist.count(word))
        counted_words.sort(key = operator.itemgetter(1))

    pie = plt.pie(cn, autopct='%1.1f%%', pctdistance=0.85)
    plt.legend(pie[0], cw, loc="center left", bbox_to_anchor = (1, 0, 0.5, 1))
    plt.title ('Study Programs ' + x)
    plt.show()


geschlecht('Männlich')
geschlecht('Weiblich')

# Function for analyzing future choices of bachelor students
## logic of the function is same as previously used function. Just the variables and type of graph are changed

def future_bachelor():
    baselist = df_bachelor['bachelor_future'].tolist()
    words = frozenset(baselist)
    print (words)
    counted_words = []
    cw= []
    cn= []
    for word in words:
        counted_words.append((word, baselist.count(word)))
        cw.append(word)
        cn.append(baselist.count(word))
        counted_words.sort(key = operator.itemgetter(1))

    explode =(0.1, 0.1, 0.1, 0.1)
    plt.pie(cn, labels = cw, explode = explode, autopct='%1.1f%%', shadow= True, startangle=90)
    plt.title ('Future Preferences of Bachelor Students')
    plt.show()
future_bachelor()

# Function for analyzing future industry preferences of bachelor students according to gender

def future_industry(x):
    a = df_bachelor['Geschlecht'] == x
    df_bachelor_tmp = df_bachelor[a]
    baselist = df_bachelor_tmp['future_work_field'].tolist()
    words = frozenset(baselist)
    print (words)
    counted_words = []
    cw= []
    cn= []
    for word in words:
        counted_words.append((word, baselist.count(word)))
        cw.append(word)
        cn.append(baselist.count(word))
        counted_words.sort(key = operator.itemgetter(1))

    fig = plt.figure()
    fig.patch.set_facecolor('black')
    plt.rcParams['text.color'] = 'white'
    pie = plt.pie(cn, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
    plt.legend(pie[0], cw, loc="center left", bbox_to_anchor = (1, 0, 0.5, 1))
    #drawing a circle in the center for donut chart
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.title ('Industrial field preferences of bachelor students - ' + x)
    plt.show()
future_industry('Männlich')
future_industry('Weiblich')

