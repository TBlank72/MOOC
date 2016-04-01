# entertainment_center.py in Movies folder
import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
									"A story of a boy and his toys",
									"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
									"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
								"A marine on an alien planet",
								"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
								"https://www.youtube.com/watch?v=d1_JBMrrYw8")

#print avatar.storyline
#avatar.show_trailer()
dazed_and_confused = media.Movie("Dazed and Confused",
													"Highschool freshman get initiated by the seniors",
													"http://www.movieposter.com/posters/archive/main/80/MPW-40398",
													"https://www.youtube.com/watch?v=3aQuvPlcB-8")
													
batman_begins = media.Movie("Batman Begins",
											"Batman defends Gotham City",
											"https://upload.wikimedia.org/wikipedia/en/a/af/Batman_Begins_Poster.jpg",
											"https://www.youtube.com/watch?v=neY2xVmOfUM")

terminator_2 = media.Movie("Terminator 2: Judgement Dat",
											"Terminators fight to save human kind",
											"https://upload.wikimedia.org/wikipedia/en/8/85/Terminator2poster.jpg",
											"https://www.youtube.com/watch?v=F1os6UU6jhU")
										
the_big_short = media.Movie("The Big Short",
											"Men capitalize on the collapse of Wall Street",
											"https://upload.wikimedia.org/wikipedia/en/e/e3/The_Big_Short_teaser_poster.jpg",
											"https://www.youtube.com/watch?v=LWr8hbUkG9s")

movies = [toy_story, avatar, dazed_and_confused, batman_begins, terminator_2, the_big_short]
#fresh_tomatoes.open_movies_page(movies)
#print media.Movie.VALID_RATINGS
print media.Movie.__doc__