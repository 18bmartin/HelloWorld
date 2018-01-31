#1.
#2. fraga-f/susa-e: the file itself for the fragments/suspects
#   frag1-6/sus1-5: the data within the suspect and fragment files
#   count: how many times a fragment appears within a suspect file
#def a counter to find fragments within suspects
def counter(a, b, c, d):
#count the fragments within the suspects
    count = a.count(b)
#get the fragment/suspect name from its file
    c = str(c)
    c = c[52:61]
    d = str(d)
    d = d[52:61]
#if the fragment has been found within the suspect print the fragment and suspect name
    if count >= 1:
        print(c, "has been located within", d)
# open fragment files
fraga = open("/users/18bmartin/documents/fragment1.txt", 'r')
frag1 = fraga.read()
fragb = open("/users/18bmartin/documents/fragment2.txt", 'r')
frag2 = fragb.read()
fragc = open("/users/18bmartin/documents/fragment3.txt", 'r')
frag3 = fragc.read()
fragd = open("/users/18bmartin/documents/fragment4.txt", 'r')
frag4 = fragd.read()
frage = open("/users/18bmartin/documents/fragment5.txt", 'r')
frag5 = frage.read()
fragf = open("/users/18bmartin/documents/fragment6.txt", 'r')
frag6 = fragf.read()

# open suspect files
susa = open("/users/18bmartin/documents/suspect1.txt", 'r')
sus1 = susa.read()
susb = open("/users/18bmartin/documents/suspect2.txt", 'r')
sus2 = susb.read()
susc = open("/users/18bmartin/documents/suspect3.txt", 'r')
sus3 = susc.read()
susd = open("/users/18bmartin/documents/suspect4.txt", 'r')
sus4 = susd.read()
suse = open("/users/18bmartin/documents/suspect5.txt", 'r')
sus5 = suse.read()

# find fragments within suspects
counter(sus1, frag1, fraga, susa)
counter(sus1, frag2, fragb, susa)
counter(sus1, frag3, fragc, susa)
counter(sus1, frag4, fragd, susa)
counter(sus1, frag5, frage, susa)
counter(sus1, frag6, fragf, susa)
counter(sus2, frag1, fraga, susb)
counter(sus2, frag2, fragb, susb)
counter(sus2, frag3, fragc, susb)
counter(sus2, frag4, fragd, susb)
counter(sus2, frag5, frage, susb)
counter(sus2, frag6, fragf, susb)
counter(sus3, frag1, fraga, susc)
counter(sus3, frag2, fragb, susc)
counter(sus3, frag3, fragc, susc)
counter(sus3, frag4, fragd, susc)
counter(sus3, frag5, frage, susc)
counter(sus3, frag6, fragf, susc)
counter(sus4, frag1, fraga, susd)
counter(sus4, frag2, fragb, susd)
counter(sus4, frag3, fragc, susd)
counter(sus4, frag4, fragd, susd)
counter(sus4, frag5, frage, susd)
counter(sus4, frag6, fragf, susd)
counter(sus5, frag1, fraga, suse)
counter(sus5, frag2, fragb, suse)
counter(sus5, frag3, fragc, suse)
counter(sus5, frag4, fragd, suse)
counter(sus5, frag5, frage, suse)
counter(sus5, frag6, fragf, suse)
