import movieClass
import freshTomatoes

#the following are variables containing the movie description
it_movie = movieClass.Movie("It 2017",
                            "A terrifying monster called 'It' haunts the children of Derry",
                            "https://s-media-cache-ak0.pinimg.com/originals/4f/16/bf/4f16bf5149792a81109b94aaf20fb844.jpg",
                            "https://youtu.be/cdg193GvnBA")


austin_powers = movieClass.Movie("Austin Powers:International Man of Mystery",
                                 "A spy sent out to stop mr. Evil",
                                 "https://goo.gl/RFkwb9",
                                 "https://youtu.be/5vsANcS4Ml8")

alien_vs_Predator = movieClass.Movie("Alien VS Predator 2004",
                                     "A number of renown architects find themselves in the middle of a war.",
                                     "http://pic.pimg.tw/yago0214/1379437376-2261581532.jpg?v=1379437377",
                                     "https://youtu.be/jC1ngKr6QA8")

aeon_flux = movieClass.Movie("Aeon Flux",
                             "An group of assassins, trying to overthrow the government runs into an issue when one of their own discovers secrets within the assassin group and the government",
                             "http://www.gstatic.com/tv/thumb/movieposters/90689/p90689_p_v8_aq.jpg",
                             "https://youtu.be/d11loPMnC2w")

the_conjuring_2 = movieClass.Movie("The Conjuring 2",
                                   "Lorraine and Ed Warren travel to help a possessed child.",
                                   "http://t3.gstatic.com/images?q=tbn:ANd9GcTW7MdBhKKtzWRoy4gtHR7YZ2hv6ln1cxpZCNwnXAR8dHPDz-eO",
                                   "https://youtu.be/KyA9AtUOqRM")

deadpool = movieClass.Movie("Deadpool",
                            "After discovering a fatal condition, Wade takes a leap of faith only to be transformed",
                            "http://t2.gstatic.com/images?q=tbn:ANd9GcTvrIHJfasS6poy34esN1O5hZonXaiqfEZb4WbnbAa9qJCIL8_9",
                            "https://youtu.be/ONHBaC-pfsk")

#this variable groups together, in an array, and portrays the movies collectively
movies = [it_movie,austin_powers, alien_vs_Predator, aeon_flux, the_conjuring_2, deadpool]
#using freshTomatoes will allow me to piggy back my code onto the already created website structure.
freshTomatoes.open_movies_page(movies)
print(movieClass.Movie.__doc__)
