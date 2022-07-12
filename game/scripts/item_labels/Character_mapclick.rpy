
label gotoLottery:
    scene mall
    show lotterygirl at right
    show finhappy at left with moveinleft
    Seller "sorry, but you can only avail once"
    return
label gotoHouseller:
    scene mall
    show financer at left
    show finneutral at right with moveinright
    Financer"What do you need from me?"
    Fin"I want some financial advice!"
    Financer"I'm sorry but I am busy at the moment"
    Fin"sorry for disturbing you"
    return
label gotoDeviceseller:
    scene Electronic_Store
    show finneutral at left with moveinleft
    show salesman at right
    Fin"I'm searching for a phone"
    Fin"Can you please help me?"
    Salesman"I'm sorry to tell you that we have no stocks left"
    Salesman"You may check some other time"
    Fin"That's sad to hear!"
    Fin"I'll come back soon!"
    Salesman"Thank you"
    return
label gotoClothesseller:
    scene Clothes_Store
    show finneutral at left with moveinleft
    show clerk at right

    Clerk"How may I help you sir?"
    Fin"I want to buy clothes that suits for me!"
    Clerk"I'm sorry to tell you we ran out of your size sir"
    Clerk"we are also waiting for new stocks coming!"
    Fin"I'll wait for it"
    Fin"Thank you!"
    return
label gotoBurgervendor:
    scene Burger_Store
    show finhappy at right with moveinright
    show waiter at left
    Waiter"Good day!"
    Waiter"what can I do for you?"
    menu:
        "eat":
            if MC.cash < 800:
                Fin"I forgot I don't have enough money to eat!"
                Waiter "Sorry to hear that but you can back here if you have money"
                Fin"Okay!"
                Waiter"Come again!"
            else:
                Waiter"You may take a seat"
                Waiter"and the best dishes will be served"
                Waiter"Just prepare 800 Pesos"
                Fin"Thank you"
                scene burgereating
                "Fin enjoys the dishes "
                $ MC.cash -= 800
    return




label gotopizzastore:
    scene pizzastore
    show francis at left
    show finneutral at right with moveinright
    Francis"It seems like you want our pizza"
    menu:
        "yes":
            if MC.cash < 50:
                Fin"I forgot I don't have enough to eat!"
                Francis "Sorry to hear that but you can back here if you have money"
                Fin"Okay!"
            else:
                Francis "It will be 50 Pesos sir!"
                Francis"Take your seat sir!"
                scene pizzaeating
                "Fin eats a fine burger in town"
                $ MC.cash -= 50
        "no":
            Francis"come visit us again sir"

    return
label gotoburgerstore:
    scene burgerstore
    show franco at left
    show finneutral at right with moveinright
    Franco"Do you want to try our pizza?"
    menu:
        "yes":
            if MC.cash < 60:
                Fin"I forgot I don't have enough to eat!"
                Francis "Sorry to hear that but you can back here if you have money"
                Fin"Okay!"
            else:
                Franco "It will be 60 Pesos sir!"

                Franco "Take your seat sir!"
                scene burgereating
                "Fin eats a fine pizza in town"
                $ MC.cash -= 60
        "no":
            Franco"come visit us again sir"
    return
label gotoschool:
    scene school
    show jorge at left
    show finneutral at right with moveinright
    Jorge"Sorry but you're still on vacation"
    Jorge"Come back soon!"
    Jorge"see you!"
    return
#label gotobank:
    #scene bank
    #show ariana at left
    #show finneutral at right with moveinright
    #Ariana"You have no business in here!"
    #return
label gotogovernment:
    scene government
    show daisy at left
    show finneutral at right with moveinright
    Daisy "You have no authority to come here"
    Daisy "Only those who have the autorith has the right to get inside!"
    return
label gotocompany:
    scene company
    show jerome at left
    show finneutral at right with moveinright
    Fin"good day! I see your bulletin outside."
    Fin"I was just wondering if you guys are hiring"
    Jerome"We're sorry to say but we are not hiring anymore applicants"
    Fin"I’m searching for a job and I would be interested in working here"
    Jerome"We will try to post again if we are hiring"
    Fin"Thank you I will be back again!"
    return
label gotofiredept:
    scene firedept
    show karter at left
    show finhappy at right with moveinright
    Karter "We don't receive any emergency yet"
    Karter "Come again if there's one!"
    return
label gotopolice:
    scene police
    show leonardo at left
    show finhappy at right with moveinright
    Leonardo "What complaint do you have?"
    menu:
        "none":
            Leonardo"So what are you doing here? Leave at once!"
    return
label gotohospital:
    scene hospital
    show nylah at left
    show finneutral at right with moveinright
    Nylah"do you have medical issue?"
    menu:
        "none":
            Fin"I'm perfectly fine"
            Fin"Just here to visit"
            Nylah"I'm happy to hear that!"
            Nylah"feel free to visit again if you want check ups"
    return
