from app.models import db, Movie, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import date
import requests



def seed_movies():
    # random movies
    randomMovie1 = Movie(
    title="The Exorcist: Believer",
    description="Two girls are possessed by a sinister force, and their parents seek out an exorcist for help.",
    release_date=date(2023, 10, 6),
    custom=False
    )

    randomMovie2 = Movie(
    title="Killers of the Flower Moon",
    description="A 1920s murder investigation into the Osage tribe killings in Oklahoma, with an FBI focus.",
    release_date=date(2023, 10, 20),
    custom=False
    )

    randomMovie3 = Movie(
    title="The Creator",
    description="A sci-fi thriller set in a future war between humanity and AI forces.",
    release_date=date(2023, 9, 29),
    custom=False
    )

    randomMovie4 = Movie(
    title="A Haunting in Venice",
    description="Detective Hercule Poirot investigates a murder during a séance.",
    release_date=date(2023, 9, 15),
    custom=False
    )

    randomMovie5 = Movie(
    title="Dumb Money",
    description="The true story of the GameStop stock explosion, led by retail investors.",
    release_date=date(2023, 9, 22),
    custom=False
    )

    randomMovie6 = Movie(
    title="Blue Beetle",
    description="Jaime Reyes finds an ancient alien scarab that transforms him into the superhero Blue Beetle.",
    release_date=date(2023, 8, 18),
    custom=False
    )

    randomMovie7 = Movie(
    title="Gran Turismo",
    description="A gamer and aspiring race car driver trains to compete in professional racing.",
    release_date=date(2023, 8, 11),
    custom=False
    )

    randomMovie8 = Movie(
    title="Haunted Mansion",
    description="A family moves into a mansion with otherworldly inhabitants, seeking help from a ghost tour guide.",
    release_date=date(2023, 7, 28),
    custom=False
    )

    randomMovie9 = Movie(
    title="Barbie",
    description="Barbie faces an existential crisis that leads her from Barbie Land to the real world.",
    release_date=date(2023, 7, 21),
    custom=False
    )

    randomMovie10 = Movie(
    title="Oppenheimer",
    description="The story of J. Robert Oppenheimer and his role in developing the atomic bomb.",
    release_date=date(2023, 7, 21),
    custom=False
    )

    randomMovies=[randomMovie1,randomMovie2,randomMovie3,randomMovie4,randomMovie5,randomMovie6,randomMovie7,randomMovie8,randomMovie9,randomMovie10]

    for random_movie in randomMovies:
        db.session.add(random_movie)
    # movies that just came out


    # api_key = '79009e38d3509a590d6510f6e91c4cd8'
    # page = 1
    # recent_movies = []
    # while True:
    #     url = f'https://api.themoviedb.org/3/movie/now_playing?api_key={api_key}&page={page}'
    #     response = requests.get(url)
    #     data = response.json()

    #     if not data['results']:
    #         break  # Exit if no more results

    #     recent_movies.append(data['results'])
    #     print(data['results'])
    #     page += 1

    # print(recent_movies)
    recentMovie1 = Movie(
    title='Transformers: One',
    description='An origin story set in the 1980s that chronicles the early days of the Transformers, exploring their home planet Cybertron and the battles that shaped their world.',
    release_date=date(2024, 9, 20),
    custom=False
)

    recentMovie2 = Movie(
    title='Beetlejuice 2',
    description='The sequel to the beloved classic where Beetlejuice returns to wreak havoc in the lives of new characters while exploring the afterlife.',
    release_date=date(2024, 9, 6),
    custom=False
)

    recentMovie3 = Movie(
    title='The Beekeeper',
    description='A former operative seeks revenge on those who wronged him, taking on a mission of justice.',
    release_date=date(2024, 1, 12),
    custom=False
)

    recentMovie4 = Movie(
    title='The Book of Clarence',
    description='A man in biblical times finds himself embroiled in events that will change history.',
    release_date=date(2024, 1, 12),
    custom=False
)

    recentMovie5 = Movie(
    title='Freud\'s Last Session',
    description='A fictional meeting between Sigmund Freud and C.S. Lewis as they debate faith and reason.',
    release_date=date(2024, 1, 12),
    custom=False
)

    recentMovie6 = Movie(
    title='Argylle',
    description='A spy thriller following the adventures of a super-spy named Argylle as he embarks on globe-trotting missions.',
    release_date=date(2024, 2, 2),
    custom=False
)

    recentMovie7 = Movie(
    title='Lisa Frankenstein',
    description='A teenage girl accidentally reanimates a Victorian corpse during a thunderstorm and they embark on a strange romance.',
    release_date=date(2024, 2, 9),
    custom=False
)

    recentMovie8 = Movie(
    title='Bob Marley: One Love',
    description='A biopic following the life and legacy of iconic musician Bob Marley.',
    release_date=date(2024, 2, 14),
    custom=False
)

    recentMovie9 = Movie(
    title='Kung Fu Panda 4',
    description='Po reunites with his long-lost family, bringing them back to the Valley of Peace as new challenges arise.',
    release_date=date(2024, 3, 8),
    custom=False
)

    recentMovie10 = Movie(
    title='Ghostbusters: Frozen Empire',
    description='The Ghostbusters team up to face a new supernatural threat that’s bringing an icy chill to the city.',
    release_date=date(2024, 3, 22),
    custom=False
)

    recentMovie11 = Movie(
    title='Godzilla x Kong: The New Empire',
    description='The iconic monsters Godzilla and King Kong must join forces against a new threat that endangers Earth.',
    release_date=date(2024, 3, 29),
    custom=False
)

    recentMovie12 = Movie(
    title='Sonic the Hedgehog 3',
    description='Sonic and his friends face new challenges and foes, continuing their adventures to save the world.',
    release_date=date(2024, 12, 20),
    custom=False
)
    recentMovies = [recentMovie1,recentMovie2,recentMovie3,recentMovie4,recentMovie5,recentMovie6,recentMovie7,recentMovie8,recentMovie9,recentMovie10,recentMovie11,recentMovie12]

    for recent in recentMovies:
        db.session.add(recent)
    # comdies
    comedy1 = Movie(
    title='Superbad',
    description='Two high school friends plan to enjoy their last weeks before graduation, leading to hilarious misadventures.',
    release_date=date(2007, 8, 17),
    custom=False
)

    comedy2 = Movie(
    title='The Hangover',
    description='A bachelor party in Las Vegas turns into a wild quest to find the missing groom after a night of heavy partying.',
    release_date=date(2009, 6, 5),
    custom=False
)

    comedy3 = Movie(
    title='Bridesmaids',
    description='A competition between a maid of honor and a bridesmaid over who is the best friend of the bride leads to comedic chaos.',
    release_date=date(2011, 5, 13),
    custom=False
)

    comedy4 = Movie(
    title='Step Brothers',
    description='Two middle-aged, lazy men become stepbrothers when their parents marry, leading to outrageous antics and rivalry.',
    release_date=date(2008, 7, 25),
    custom=False
)

    comedy5 = Movie(
    title='Groundhog Day',
    description='A weatherman finds himself living the same day over and over, forcing him to reevaluate his life and choices.',
    release_date=date(1993, 2, 12),
    custom=False
)

    comedy6 = Movie(
    title='Mean Girls',
    description='A teenage girl navigates high school cliques and friendships, facing the challenges of fitting in and being true to herself.',
    release_date=date(2004, 4, 30),
    custom=False
)

    comedy7 = Movie(
    title='Dumb and Dumber',
    description='Two dim-witted friends embark on a cross-country trip to return a briefcase full of money to its owner, leading to outrageous situations.',
    release_date=date(1994, 12, 16),
    custom=False
)

    comedy8 = Movie(
    title='21 Jump Street',
    description='Two underperforming police officers go undercover as high school students to crack a drug ring, leading to comedic moments.',
    release_date=date(2012, 3, 16),
    custom=False
)

    comedy9 = Movie(
    title='The 40-Year-Old Virgin',
    description='A middle-aged man who has never had sex tries to change his life with the help of his friends, leading to awkward and funny situations.',
    release_date=date(2005, 7, 15),
    custom=False
)

    comedy10 = Movie(
    title='Zoolander',
    description='A dim-witted male model is brainwashed to assassinate the Prime Minister of Malaysia while trying to save the fashion industry.',
    release_date=date(2001, 9, 28),
    custom=False
)

    comedyMovies = [
    comedy1,
    comedy2,
    comedy3,
    comedy4,
    comedy5,
    comedy6,
    comedy7,
    comedy8,
    comedy9,
    comedy10
]
    for comedy in comedyMovies:
        db.session.add(comedy)
    # horror movies
    horror1 = Movie(
    title='Hereditary',
    description='A family uncovers dark secrets about their ancestry after the death of their secretive grandmother, leading to tragic and terrifying consequences.',
    release_date=date(2018, 6, 8),
    custom=False
)

    horror2 = Movie(
    title='Get Out',
    description='A young African American man discovers a disturbing secret when he visits his white girlfriend’s family for the weekend.',
    release_date=date(2017, 2, 24),
    custom=False
)

    horror3 = Movie(
    title='A Quiet Place',
    description='In a post-apocalyptic world, a family must live in silence to avoid blind monsters that hunt by sound.',
    release_date=date(2018, 4, 6),
    custom=False
)

    horror4 = Movie(
    title='The Conjuring',
    description='Paranormal investigators help a family terrorized by a dark presence in their farmhouse.',
    release_date=date(2013, 7, 19),
    custom=False
)

    horror5 = Movie(
    title='It Follows',
    description='A young woman is pursued by a supernatural entity after a sexual encounter, leading to an overwhelming sense of dread.',
    release_date=date(2014, 3, 27),
    custom=False
)

    horror6 = Movie(
    title='Midsommar',
    description='A couple travels to Sweden for a festival that only happens every 90 years, but they become entangled in disturbing pagan rituals.',
    release_date=date(2019, 7, 3),
    custom=False
)

    horror7 = Movie(
    title='The Witch',
    description='A Puritan family in 1630s New England encounters forces of evil in the woods beyond their farm.',
    release_date=date(2015, 2, 19),
    custom=False
)

    horror8 = Movie(
    title='Us',
    description='A family is confronted by their doppelgängers in a terrifying fight for survival during their vacation.',
    release_date=date(2019, 3, 22),
    custom=False
)

    horror9 = Movie(
    title='Sinister',
    description='A true-crime writer discovers a cache of home movies that depict gruesome murders and uncover a dark presence.',
    release_date=date(2012, 10, 12),
    custom=False
)

    horror10 = Movie(
    title='The Babadook',
    description='A widowed mother and her son are haunted by a sinister presence that emerges from a mysterious book.',
    release_date=date(2014, 5, 22),
    custom=False
)

    horrorMovies = [
    horror1,
    horror2,
    horror3,
    horror4,
    horror5,
    horror6,
    horror7,
    horror8,
    horror9,
    horror10
]
    for horror in horrorMovies:
        db.session.add(horror)
# romance
    romance1 = Movie(
    title='The Notebook',
    description='A sweeping love story that follows a couple who fall in love during the early years of World War II.',
    release_date=date(2004, 6, 25),
    custom=False
)

    romance2 = Movie(
    title='Pride and Prejudice',
    description='An adaptation of Jane Austen’s classic novel, focusing on the complex relationship between Elizabeth Bennet and Mr. Darcy.',
    release_date=date(2005, 11, 11),
    custom=False
)

    romance3 = Movie(
    title='La La Land',
    description='A jazz musician and an aspiring actress fall in love but struggle to maintain their relationship amidst their individual pursuits.',
    release_date=date(2016, 12, 9),
    custom=False
)

    romance4 = Movie(
    title='A Walk to Remember',
    description='A rebellious teenager falls in love with a quiet, religious girl, leading to a profound transformation in his life.',
    release_date=date(2002, 1, 25),
    custom=False
)

    romance5 = Movie(
    title='Titanic',
    description='A fictionalized account of the ill-fated voyage of the RMS Titanic, focusing on a romance between a rich girl and a poor artist.',
    release_date=date(1997, 12, 19),
    custom=False
)

    romance6 = Movie(
    title='Crazy, Stupid, Love',
    description='A man’s life changes after his wife asks for a divorce; he learns dating tips from a bachelor and begins navigating the dating scene.',
    release_date=date(2011, 7, 29),
    custom=False
)

    romance7 = Movie(
    title='The Fault in Our Stars',
    description='Two teenagers with cancer fall in love and embark on an adventure to find a reclusive author.',
    release_date=date(2014, 6, 6),
    custom=False
)

    romance8 = Movie(
    title='10 Things I Hate About You',
    description='A modern adaptation of Shakespeare’s "The Taming of the Shrew," focusing on the challenges of teenage love.',
    release_date=date(1999, 3, 31),
    custom=False
)

    romance9 = Movie(
    title='Notting Hill',
    description='A chance encounter between a famous actress and a bookstore owner leads to an unexpected romance.',
    release_date=date(1999, 5, 28),
    custom=False
)

    romance10 = Movie(
    title='When Harry Met Sally...',
    description='The film explores the question of whether men and women can be just friends while navigating romantic relationships.',
    release_date=date(1989, 7, 21),
    custom=False
)
    romanceMovies = [
    romance1,
    romance2,
    romance3,
    romance4,
    romance5,
    romance6,
    romance7,
    romance8,
    romance9,
    romance10
]
    for ro in romanceMovies:
        db.session.add(ro)
# scifi
    sciFi1 = Movie(
    title='Inception',
    description='A skilled thief is given a chance to have his criminal history erased if he can successfully perform inception: planting an idea into a target’s subconscious.',
    release_date=date(2010, 7, 16),
    custom=False
)

    sciFi2 = Movie(
    title='Blade Runner 2049',
    description='A new blade runner unearths a long-buried secret that has the potential to plunge what’s left of society into chaos.',
    release_date=date(2017, 10, 6),
    custom=False
)

    sciFi3 = Movie(
    title='The Matrix',
    description='A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.',
    release_date=date(1999, 3, 31),
    custom=False
)

    sciFi4 = Movie(
    title='Interstellar',
    description='A team of explorers travels through a wormhole in space in an attempt to ensure humanity’s survival.',
    release_date=date(2014, 11, 7),
    custom=False
)

    sciFi5 = Movie(
    title='Star Wars: Episode IV - A New Hope',
    description='A young farm boy becomes embroiled in a galactic battle against an evil empire after discovering a hidden message from a princess.',
    release_date=date(1977, 5, 25),
    custom=False
)

    sciFi6 = Movie(
    title='Arrival',
    description='A linguist is recruited to communicate with extraterrestrial beings after twelve mysterious spacecraft appear around the world.',
    release_date=date(2016, 11, 11),
    custom=False
)

    sciFi7 = Movie(
    title='Ex Machina',
    description='A young programmer is selected to participate in a groundbreaking experiment in synthetic intelligence by evaluating a highly advanced A.I.',
    release_date=date(2015, 4, 10),
    custom=False
)

    sciFi8 = Movie(
    title='The Fifth Element',
    description='In the 23rd century, a cab driver becomes an unlikely hero in the fight to save the world from an ancient evil.',
    release_date=date(1997, 5, 9),
    custom=False
)

    sciFi9 = Movie(
    title='Dune',
    description='In a distant future, the son of a noble family becomes embroiled in a battle over a precious resource on a desert planet.',
    release_date=date(2021, 10, 22),
    custom=False
)

    sciFi10 = Movie(
    title='Eternal Sunshine of the Spotless Mind',
    description='After a painful breakup, a couple undergoes a procedure to erase memories of each other, only to realize they still have feelings for one another.',
    release_date=date(2004, 3, 19),
    custom=False
)
    sciFiMovies = [
    sciFi1,
    sciFi2,
    sciFi3,
    sciFi4,
    sciFi5,
    sciFi6,
    sciFi7,
    sciFi8,
    sciFi9,
    sciFi10
]
    for sci in sciFiMovies:
        db.session.add(sci)

    action1 = Movie(
    title='Mad Max: Fury Road',
    description='In a post-apocalyptic wasteland, a woman rebels against a tyrannical ruler while trying to survive with a group of female prisoners.',
    release_date=date(2015, 5, 15),
    custom=False
)

    action2 = Movie(
    title='John Wick',
    description='An ex-hitman comes out of retirement to track down the gangsters that took everything from him.',
    release_date=date(2014, 10, 24),
    custom=False
)

    action3 = Movie(
    title='Die Hard',
    description='A New York City police officer must save his wife and several others taken hostage by terrorists during a Christmas party.',
    release_date=date(1988, 7, 20),
    custom=False
)

    action4 = Movie(
    title='The Dark Knight',
    description='Batman faces his greatest challenge yet as he battles the Joker, a criminal mastermind intent on causing chaos in Gotham City.',
    release_date=date(2008, 7, 18),
    custom=False
)

    action5 = Movie(
    title='Gladiator',
    description='A betrayed Roman general seeks revenge against the corrupt emperor who murdered his family and sent him into slavery.',
    release_date=date(2000, 5, 5),
    custom=False
)

    action6 = Movie(
    title='The Avengers',
    description='Earth’s mightiest heroes must come together to stop an extraterrestrial invasion led by Loki, the god of mischief.',
    release_date=date(2012, 5, 4),
    custom=False
)



    action8 = Movie(
    title='Transformers',
    description='Humans and alien robots clash as a war for the AllSpark escalates on Earth, involving ancient and powerful forces.',
    release_date=date(2007, 7, 3),
    custom=False
)

    action9 = Movie(
    title='Casino Royale',
    description='James Bond embarks on his first mission as 007 to bankrupt a terrorist financier in a high-stakes poker game.',
    release_date=date(2006, 11, 14),
    custom=False
)

    action10 = Movie(
    title='Mission: Impossible - Fallout',
    description='Ethan Hunt and his IMF team must track down stolen plutonium while facing the consequences of his past actions.',
    release_date=date(2018, 7, 27),
    custom=False
)
    actionMovies = [
    action1,
    action2,
    action3,
    action4,
    action5,
    action6,
    action8,
    action9,
    action10
]
    for action in actionMovies:
        db.session.add(action)

    db.session.commit()




def undo_movies():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.movies RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM movies"))

    db.session.commit()
