Bloc n°5 : Industrialisation d'un algorithme d'apprentissage automatique et automatisation des processus de décision.

Contact: Arnaud DALAIS E-mail : arnaud.dalais@free.fr

Video link : 👉 👈

Subject:

In order to mitigate those issues we’ve decided to implement a minimum delay between two rentals. A car won’t be displayed in the search results if the requested checkin or checkout times are too close from an already booked rental.

It solves the late checkout issue but also potentially hurts Getaround/owners revenues: we need to find the right trade off.

Our Product Manager still needs to decide:

    threshold: how long should the minimum delay be?
    scope: should we enable the feature for all cars?, only Connect cars?

In order to help them make the right decision, they are asking you for some data insights. Here are the first analyses they could think of, to kickstart the discussion. Don’t hesitate to perform additional analysis that you find relevant.

    Which share of our owner’s revenue would potentially be affected by the feature How many rentals would be affected by the feature depending on the threshold and scope we choose?
    How often are drivers late for the next check-in? How does it impact the next driver?
    How many problematic cases will it solve depending on the chosen threshold and scope?

You can find the whole description of the project in 2 steps:

Step 1 EDA and dashboard:
you can find the EDA on getaround_EDA.ipynb and on app.py for the dashboard
you can go on https://getaround-dash.herokuapp.com/ 

Step 2 Machine Learning and API:
you can find the Machine learning project on getaround_ML.ipynb and the api on api.py or on 
https://getaround-ap.herokuapp.com/ i have also add api_request.ipynb if you want to try on a notebook 


