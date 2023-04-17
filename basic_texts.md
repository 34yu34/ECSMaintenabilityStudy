
# On the maintenability of ECS and Object-Oriented programming in video gamess, and empirical study 

# abstract

# Introduction

Video game development has always been a world where performance dictates the bests.
Since the creation of DOOM up to the newest Assasins Creed, we try to squash every bit of performance from both the CPU and GPU in order to obtain the best graphics, realistic AIs, accurate physics and a fluid experience for the player. to achieve this effect, so many different architecture have been implemented and tests.For example, Doom used a model based aproach, Unreal engine uses a super class architecture and Unity uses a component base arctitecture. However all of these have been develop with performance as the core concern. All of these uses Object Oriented Programming as the way to go to develop the games.

However, recently, data-oriented programming, more specifically ECS or Entity-Component-System, have surfaced as the newest and most performant architecture one can use to develop video game. A couple of solution have came out most notable of which being the DOTS framework offered by unity which just recently launch the 1.0 version. Some notorious game that used such engine includes Overwatch, Fortnite, Hearthstonea and Star Citizen. As more and more actors in the industry start to use it, it becomes important to better understand this framework to make the better use of it.

It is important to note, that while ECS is considered a great programming framework, most of the game that use it do not exclusively use it. Consequently, object oriented-programming might still be use in a lot of those projects.

Software engineering has developed a great amount of methods in object-oriented programing to make programs more maintenable. From video game specific artecture to video game specific design pattern. However, not as much work and research as been put into the different facet of ECS and how it truly compares to the industry-approved    

in this work, 

# Related Work

Works on the subject of Object Oriented programming in video games are everywhere. 

# Methodology

this paper tries to better understand ECS project and the maintenability of such programs. To attain this effect,  I will use object oriented programing (OOP) as the baseline on which ECS framework shall be compare. Since the industry has used OOP a lot, it will be easier to see what place ECS takes, and how it performs.

I shall look on two different metric inside common open source video game projects (plugins or games) using ECS or Object oriented framework. First one will be the changeproness defined as the frequency of a file to be change. To calculate this metric we will look at the average amount of change a file from any project from its creation to its last version. Since longer projects will tend to have more changes per files, we shall divide this metric by a time base dampening factor.
equation : 
To get find this information, I will use an automated approach that will count the presence of files in each commit of the projects. A file being present in a commit means it has been either created, modified (Changed) or destroyed. Since every file will have to be created, we shall reduce the the amount of change by 1.

the second section will look at faultproness of files 

# Results

# Discussion

# Validity

# References
1. Gamma, E., Helm, R., Johnson, R.,, Vlissides, J. M. (1994). Design Patterns: Elements of Reusable Object-Oriented Software. Addison-Wesley Professional. ISBN: 0201633612

2. Ceruzzi, P. E. (2003). A history of modern computing. MIT press.

3. Wexelblat, R. L. (Ed.). (2014). History of programming languages. Academic Press.

4. Hansen, H., & Öhrström, O. (2020). Benchmarking and Analysis of Entity Referencing Within Open-Source Entity Component Systems.