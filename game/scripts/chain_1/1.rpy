label chain_1_0:
    scene fronthouse
    show finhappy at left with moveinleft
    "Fin calls Tuan"
    "The phone rings"
    hide finhappy

    show fincalling at left
    Tuan "Hello my friend"
    Fin "I have a great news to you Tuan!"
    Fin "I Won a 10,000 Pesos here at the mall in the lottery stall here"
    Tuan "Wow that’s great. Congrats Fin"
    Fin "Thankyou Tuan can you come over let's celebrate"
    Tuan "Okay Fin"
    hide fincalling
    show tuanhappy at right with moveinright
    show finhappy at left
    "Fin start’s to think that is it not bad to celebrate"
    Fin "Maybe it’s not bad to celebrate for what I have achieved"
    Fin "And also it's just for once"
    Tuan "Hey Fin let’s go stop thinking twice"
    Tuan "This is your chance to be happy and buy what you want "
    "After that Fin and Tuan goes to the mall to celebrate the winning of Fin"
    hide tuanhappy
    hide finhappy
    $Chain[0].next()
    return
label chain_1_1:
    scene mall

    show tuanhappy at right
    show finhappy at left
    Fin "Hey Tuan it’s so nice here at the mall right?"
    Fin"There are so many things here that I can buy"
    Fin "And Pay with this money, Would you help me?"
    Tuan "Yes right Fin this place is one of the best places in our Town"
    Tuan "To Spend that money"
    Tuan "Of course it will just ne a piece of cake"
    Tuan "friend Fin"
    Tuan "Now we are in the Mall first we will look for things to buy for you"
    Tuan "Besides you won a lot of Money right?"
    Tuan"I'll take care of you all with nice clothes"
    Tuan"And a nice kind of phone"
    Tuan"So that you don't have to use your old phone."
    Tuan "How about let’s try to look at the Electronic Shop"
    Tuan "I heard that there are new phones that has been released last week"
    Fin"Is that so?"
    Fin"Go ahead as long as you take care of everything I need okay?"
    Tuan"Yes I will take care of you"
    Fin"Okay Tuan i’ll follow you"
    hide tuanhappy at right
    hide finhappy at left
    scene Electronic_Store
    show salesman at center
    Salesman "Hi sir, What are they looking for?"
    show finneutral at left
    show tuanneutral at right
    Tuan "What is your brand new phones?"
    Salesman "We have this phone that costs 2,700 Pesos"
    Salesman"It's beautiful because it has 6gb of ram"
    Salesman"And 128gb of Internal Storage"
    Salesman "It has good Specs, It also takes a long time to run out of battery"
    Salesman "And most of all it also charge quickly. "
    Salesman "We also have this phone that costs 2,700 Pesos too "
    Salesman"It's nice because it still has 4gb of ram"
    Salesman"but 256 gb of Internal Storage"
    Salesman "It has good specs, It also takes a long time to run out of battery"
    Salesman "and most of all it also charge quickly"
    hide finneutral at left
    show finthinking at left


    menu:
        "Okay i'll buy the first one":
            hide finthinking
            show finneutral at left
            Tuan "Buy that Fin"
            Tuan"There's nothing else to find on that phone"
            Tuan "Everything is already there"
            Tuan"And you may be aware that they also have freebies on offer"
            Tuan "Sir do you have freebies when we buy that?"
            Salesman "Yes sir."
            Salesman"There is, when you buy now you will also receive some of the gadgets"
            Salesman"That we also have, like Earphones, Speakers... so on and so forth"
            Salesman" It's up to you to choose what freebies you want"
            Fin"All right, I'll buy that one. You just choose the freebies for me"
            Salesman "Thank you very much sir, God bless"
            Fin "Hey Tuan do I look skinny in this T-Shirt?"
            Tuan "Not much!"
            Tuan"But I know a place where we can get desireable clothes"
            Tuan"It’s right around the corner"
            Tuan"Fin I see something new clothes store here in mall"
            Tuan"they sell it on half price and all branded"
            Tuan"Do You Want to window shopping?"
            Fin "Mmm, Okay"
            Fin"Let's go there."
            Fin"But before that I Will Pay for my phone first."
            Fin"How much for the phone again sir?"
            Salesman"It is 2,700 Pesos only sir!"
            Fin"Here's the 2,700 Pesos"
            $ MC.cash -= 2700
            hide salesman at center
        "Okay I'll buy the Second one":
            hide finthinking
            show finneutral at left
            Tuan "Buy that Fin"
            Tuan"There's nothing else to find on that phone"
            Tuan "Everything is already there"
            Tuan"And you may be aware that they also have freebies on offer"
            Tuan "Sir do you have freebies when we buy that?"
            Salesman "Yes sir."
            Salesman"There is, when you buy now you will also receive some of the gadgets"
            Salesman"That we also have, like Earphones, Speakers... so on and so forth"
            Salesman" It's up to you to choose what freebies you want"
            Fin"All right, I'll buy that one. You just choose the freebies for me"
            Salesman "Thank you very much sir, God bless"
            Fin "Hey Tuan do I look skinny in this T-Shirt?"
            Tuan "Not much!"
            Tuan"But I know a place where we can get desireable clothes"
            Tuan"It’s right around the corner"
            Tuan"Fin I see something new clothes store here in mall."
            Tuan"they sell it on half price and all branded"
            Tuan"Do You Want to window shopping?"
            Fin "Mmm, Okay"
            Fin"Let's go there."
            Fin"But before that I Will Pay for my phone first"
            Fin"How much for the phone again sir?"
            Salesman"It is 2,700 Pesos only sir!"
            Fin"Here's the 2,700 Pesos"
            $ MC.cash -= 2700
            hide salesman at center
    scene Clothes_Store

    show finhappy at left with moveinleft
    show tuanhappy at right with moveinright

    Tuan"Fin I think it is fit for uou"
    Tuan"Do you want it for yourself"
    Fin"Wait, Im just thinking about the design and the size for me"
    show clerk at center with dissolve
    Clerk "Good day!"
    Clerk"What do you want?"
    Clerk"We have a lot of stocks here"
    Clerk"So you can choose anyone of that"
    Tuan"I will guide you to choose"
    Tuan"Come on! "
    Tuan"Let’s see other designs"
    Fin"Okay I will follow"
    Clerk"In this area sir we have a limited edition of clothes"
    Clerk"So what do you think? Do you like it?"
    Tuan"Oh my god Fin!"
    Tuan "It is so very cool"
    Tuan"I think it is the best and it will suit you"
    Tuan"Come on fin"
    Tuan"You need to try it. Let's go to the fitting room "
    hide finhappy at left
    show Clothes_2 at left
    Fin"Yeah, it is so nice and I like it"
    Tuan"I knew it right"
    Tuan"You haven't worn it yet"
    Tuan"But I know it's fit to you"
    Tuan"It's so beautiful to look at your new shirt"
    Fin"Okay I will get this"
    Fin"Just wait for me and I'm going To counter to pay for this"
    Fin"How much is the cost ma'am?"
    Clerk "You just need to pay 1,500 Pesos over the counter sir!"
    $ MC.cash -= 1500
    hide Clothes_2 at left
    Clerk "I hope your friend will like all the clothes he bought sir!"
    Tuan"I really hope that too!"
    show finhappy at left
    Clerk"Thank you so much for availing sir."
    Clerk"Have a good day!"
    hide clerk at center
    scene mall
    show finneutral at left
    show tuanneutral at right
    Fin"Hey Tuan I'm getting hungry, Do you know a place where we can eat fancy dishes?"
    Tuan"Yes Fin I know a place where we can eat follow me"
    scene Burger_Store
    "After buying clothes and a new phone"
    "Fin and Tuan already experiencing hunger while shopping for clothes"
    "So they decided to eat"
    show finhappy
    show tuanhappy at right
    Tuan"Let's just come here and more delicious food here"
    Tuan"I know you'll love it"
    Tuan"And you repeat over and over the food here"
    Fin"Let's see."
    show waiter at left
    Waiter" Good day!"
    Waiter"What is your order?"
    Tuan"I know a good food in Here and that's what i'd like you to try"
    Fin"Let me try that for"
    Waiter"Yes Sir!"
    Waiter"We are to serve the best seller food"
    Fin"Oh I really can't wait to see and try that"
    Tuan"Fin it is good to buy best seller food"
    Tuan"For you to taste delicious food"
    Tuan"It's only once"
    Tuan"And to celebrate as well, may I right!"
    Fin"At least you have a point"
    Fin"Okay let’s order now"
    show malleating
    "Fin and Tuan eating a lot like they were so tired roaming at the mall"
    Fin"I will call the waiter to bill out "
    Fin"Waiter!"
    Fin"Bill out!"
    show waiter at left with moveinleft
    Waiter"It's 800 Pesos sir!"
    Fin"here's the 800 Pesos!"
    $ MC.cash -= 800

    hide waiter at center
    scene mall
    show tuanhappy at right with moveinright
    show finhappy at left with moveinleft
    Tuan"Thank you so Much fin for this"
    Tuan"Hey Fin I wanna ask you something"
    Fin"What is it Tuan?"
    Tuan"How’s the feeling of having so much money?"
    Fin"Technically speaking Tuan"
    Fin"It's great because I can buy all the things that I want"
    Fin"But it’s very hard to manage your money Tho"
    Fin"Me having this kind of money really makes my head confuse"
    Fin"Because there’s this things that I want and i need"
    Tuan"Yes fin, actually my mom is also having a hard time with her money"
    Fin"Maybe we can ask someone"
    Fin"I saw at the mall that there’s a stall where they teach kids and teenagers"
    Fin"About financial literacy"
    Tuan"Wow Fin, it’s fine for me lead the way"
    show financer
    Fin"Hello sir, are you the one teaching about financial literacy?"
    Financer"Yes I am the one"
    Financer" What's up?"
    Financer"By the way I'm Literet Garcia But you can call me mr.Literet"
    Fin"Hello sir I'm Fin and this is my friend Tuan"
    Financer"So what brings you here son?"
    Fin"We heard that your teaching about financial literacy"
    Fin"And also we want to more about budgeting money"
    Fin"Since I'm struggling budgeting my own money"
    Financer"Is that so fin?"
    Financer"Okay maybe I can teach you Basics"
    Financer"First we will start knowing what is financial literacy"
    Financer"Financial Literacy is the ability to understand and effectively
            Use Various Financial Skills, Including personal financial management,
             budgeting And investing"
    Financer"Financial Literacy is the foundation of your relationship with money"
    Financer"And it is a lifelong journey of learning"
    Financer"It Means Fin it’s a skill of knowing the idea of organizing your money"
    Financer"Like a talent somehow"
    Fin"That’s a deep one Mr.Literet"
    Fin"But how will we know the proper way of budgeting our Money"
    Financer"Before you start budgeting your money tou have to know the 2 Categories"
    Financer"It’s the needs and the wants"
    Financer"The needs thing that you have to pay is Basically the one that Has
    More value to your life like bills, Food, Shelter, Education And Medicines"
    Financer" In a simple way need things are the one’s you are using
    For the rest of your life"
    Fin"Oh now I get it Mr. Literet"
    Fin"But how about the wants?"
    Financer"The wants thing are commonly the things that makes you even more happy"
    Financer" Like your phone, your new clothes, fancy vacations And other things that are not so important"
    Financer" Wants thing is not that valuable in life because we can afford it only if we have that much money"
    Financer"Knowing the difference about needs and wants will build your idea about budgeting and will help you organize money"
    Fin"Ohhh so it means this phone that I bought is not important because I have another phone that I'm still using?"
    Financer"Yes Fin that’s right"
    Financer"You know life is just a matter of being contented on what you want"
    Fin"That’s nice Mr.Literet thank you for uour ideas we really appreciate it so much"
    Fin"We will go now thank you again"
    "After having a great day at the mall and talking to Mr. Literet"
    " Fin and Tuan decided to go back on their own home"
    Fin"Tuan I'm tired maybe we should go back home"
    Tuan"Okay Fin I think we have enough bonding for this day"
    Fin"Hey Tuan you know Mr.Literet is a great educator about money. "
    Fin"I really learn something a lot from him"
    Tuan"Me too Fin, soon when I have my money of my own I know what to do with it"
    Tuan"My house ss near Fin, see you next time bro "
    Tuan"Thank you for the treat friend"
    Fin"Of course Fin my pleasure "
    Fin"You’re Welcome"
    $Chain[0].next()
    return


label chain_1_2:
    scene Sleeping
    "After a long day with tuan fin arrives home very tired and want to get some sleep so he decided to go to his bedroom and sleep"

    scene fronthouse
    "A Night Pass and a very long might for Fin ended"
    "It’s a bright new day again for Fin"
    show finhappy with moveinleft
    Fin"Good morning self it’s a brand new day for me"
    "Fin has a great wake up when his phone suddenly rings?"
    hide finhappy
    show fincalling
    Fin"Hello who is this?"
    Caller"This is rex from billing department
     We would like to inform you that you have a
       bill, for the electricity is 1000 Pesos
      and for the water is 800 Pesos a total of 1800 Pesos Sir"
    Fin" (In his mind “oh no I forgot about The upcoming bills how am I gonna budget my last money”) "
    Fin"Okay Sir i’ll take note for that"
    hide fincalling
    show finsad
    "then his phone rings again"
    hide finsad
    show fincalling
    Tuan"Hello Fin"
    Fin"Hello Tuan"
    Tuan"I Heard there’s a brand new toy robot at the mall wanna buy some"
    Tuan"It’s a very special toy fin"
    menu:
        "reject":
            Fin"I don’t know tuan"
            Fin"I have some problems here at the house"
            Fin"I forgot that I need to pay for the Electricity And Water Bill"
            Tuan"That’s bad Fin but still it’s a great toy Fin"
            Fin"Yeah I Know Tuan but I have to solve this problem’s first I only have [MC.cash] left on my money what should I do
            and I Don’t have enough food."
            Fin"I really have to go bank right now!"
            Fin"before I spend this money"
            Tuan"I'm not happy to hear to that"
            Tuan"but I understand"
            Fin"thanks tuan, I really appreciate it, see you again"
            Tuan"You're welcome"
        "Accept":
            Fin"Let's go, I'm going to buy that toy"
            Tuan"FIN!!!!"
            Tuan"I'm just kidding!"
            Tuan"Don't you have any upcoming bills?"
            Tuan"I'm pretty sure and my instinct telling me you have"
            Fin"yeah i really have upcoming bills!"
            Tuan"Make your bills be priority always fin"
            Fin"yeah, Thanks for reminding me"
            Fin"You're a good friend!"




    $Chain[0].next()
    return
label chain_1_3:
    scene bank
    show finneutral at right with moveinright
    show ariana at left
    Fin"Good day Ma'am"
    Ariana"Hi sir how can I help you?"
    Fin"I would like to pay for my bills."
    Fin"Can you check my account and the balances that I have?"
    Ariana"Yes sir, Please Wait"
    Fin"okay thank you"
    Ariana"Mr.Fin as of our system you still have a remaining balance last month of 2200 pesos for the electricity and for the water  then a 1000 pesos for the internet and also your payment for this month is 1800 so the sum of it all is 5000 pesos sir."
    Fin"Oh yes, It's good that I rejected Tuan to go to mall"
    Fin"or else my money will not be enough"
    Fin"Sorry for interuption madam"
    Fin"I'm just happy that I did the right thing"
    Fin"and here's the payment"
    if MC.cash >= 5000:
        Ariana"Thank you sir"
        scene conclusion
        pause 5
        $ renpy.quit()

    else:
        Ariana"I'm very sorry sir but you don't have enough money to pay us"
        Ariana"and I'm sorry to tell you that we're to take back your electricities, water and  internet connection!"
        hide finneutral
        show finsad at right
        Fin"I'm sorry because I carried away of my stuff"
        Ariana"Sorry to hear that sir but there's nothing I can do for you"
        Fin"It's okay"
        scene conclusion2
        pause 5
        $ renpy.quit()

    scene conclusion
    pause 5
    $ renpy.quit()





    $Chain[0].next()
    return
label chain_1_4:
    "Event 3 started"
    $Chain[0].next()
    return
label chain_1_5:
    "Event 3 started"
    $Chain[0].next()
    return
label chain_1_6:
    "Event 3 started"
    $Chain[0].next()
    return
label chain_1_7:
    "Event 3 started"
    $Chain[0].next()
    return
label chain_1_8:
    "Event 3 started"
    $Chain[0].next()
    return
label chain_1_9:
    "Event 3 started"
    $Chain[0].next()
    return
