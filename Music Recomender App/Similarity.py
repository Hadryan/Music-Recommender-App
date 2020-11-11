import pandas as pd
from rdflib import Graph, Literal, URIRef
from rdflib.namespace import RDFS,FOAF,OWL
from langdetect import detect
from DataMusic import MusicList
import nltk



MusicList = MusicList()
def similar(title):
    similarSong=""
    #Find the selected song from the music list
    for song in MusicList:
        if song.title == title:
            myTitle = song.title
            myUri = song.uri
            myDecade = song.decade
            myGenres = song.genre.split()

        # Compare with the rest of the songs by genre
    sameGenres = []
    for song in MusicList:
        if song.title != myTitle: #ovoj if mi e da ne ja stavam mojata pesna
            gen = []
            gen = song.genre.split()
            if set(myGenres) == set(gen):
                sameGenres.append(song.uri)


    #If there are other songs with the same genre
    if len(sameGenres) != 0:
        #lista so pesni od istata dekada i ist genre
        sameDecade= []
        for sg in sameGenres:
            for song in MusicList:
                if sg == song.uri:
                    if myDecade == song.decade:
                        sameDecade.append(song.uri)

      # najdi  abstract na sameDecade (tie se ista dekada i ist genre)
        g = globals()
        i = 0
        abstract = URIRef("http://dbpedia.org/ontology/abstract")
        abstract_dict = {}
        for sd in sameDecade:
            graph = Graph()
            graph.parse(sd)
            for s, p, o in graph.triples((None, abstract, None)):
                if detect(o) == 'en':
                    obje = o
            abstract_dict[sd] = obje
            g['graph_{0}'.format(i)] = graph
            i += 1

        # najdi go mojot abstract
        myGraph = Graph()
        myGraph.parse(myUri)
        for s, p, o in myGraph.triples((None, abstract, None)):
            if detect(o) == 'en':
                obje = o
                myAbstract = obje

        max_similarity = 0
        maxsimURI = ""

        for sd in sameDecade:
            #najdi go abstractot za sekoj od listata na sameDecade vo dic od abstracti so ist genre i najdi max jaccard similarity
            for key in abstract_dict.keys():
                if sd == key:
                    similarity = nltk.jaccard_distance(set(myAbstract.split()), set(abstract_dict[key].split()))
                    if similarity > max_similarity:
                        max_similarity = similarity
                        maxsimURI = key
        for song in MusicList:
            if maxsimURI == song.uri:
                similarSong= song.title



    #ako nema druga pesna so ist genre kako selektiranata(mojata)
    else:

        # lista so pesni od ista dekada ali ne ist ganre
        sameDecade = []
        for song in MusicList:
            if (myTitle != song.title) and (myDecade == song.decade):
                sameDecade.append(song.uri)

        g = globals()
        i = 0

        abstract = URIRef("http://dbpedia.org/ontology/abstract")
        abstract_dict = {}
        for sd in sameDecade:
            graph = Graph()
            graph.parse(sd)
            for s, p, o in graph.triples((None, abstract, None)):
                if detect(o) == 'en':
                    obje = o
            abstract_dict[sd] = obje
            g['graph_{0}'.format(i)] = graph
            i += 1

        # najdi go mojot abstract
        myGraph = Graph()
        myGraph.parse(myUri)
        for s, p, o in myGraph.triples((None, abstract, None)):
            if detect(o) == 'en':
                obje = o
                myAbstract = obje



        max_similarity = 0
        maxsimURI = ""

        for sd in sameDecade:
            # najdi go abstractot za sekoj od listata na sameDecade vo dic od abstracti so ist genre i najdi max jaccard similarity
            for key in abstract_dict.keys():
                if sd == key:
                    similarity = nltk.jaccard_distance(set(myAbstract.split()), set(abstract_dict[key].split()))
                    if similarity > max_similarity:
                        max_similarity = similarity
                        maxsimURI = key
        for song in MusicList:
            if maxsimURI == song.uri:
                similarSong = song.title



    return (similarSong)


    FinalDict = {}
    for song in MusicList:
        similarM = similar(song.title)
        FinalDict[song.id] = similarM


    similarM=similar("Umbrella")
    print(similarM)









