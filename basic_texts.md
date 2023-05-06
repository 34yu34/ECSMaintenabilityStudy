
# On the maintenability of ECS and Object-Oriented programming in video games, an empirical study 

# abstract

# Introduction

Video game development has always been a world where performance dictates the bests.
Since the creation of DOOM up to the newest Assasins Creed, we try to squash every bit of performance from both the CPU and GPU in order to obtain the best graphics, realistic AIs, accurate physics and a fluid experience for the player. to achieve this effect, so many different architecture have been implemented and tests.For example, Doom used a model based aproach, Unreal engine uses a super class architecture and Unity uses a component base arctitecture. However all of these have been develop with performance as the core concern. All of these uses Object Oriented Programming as the way to go to develop the games.

However, recently, data-oriented programming, more specifically ECS or Entity-Component-System, have surfaced as the newest and most performant architecture one can use to develop video game. A couple of solution have came out most notable of which being the DOTS framework offered by unity which just recently launch the 1.0 version. Some notorious game that used such engine includes Overwatch, Fortnite, Hearthstonea and Star Citizen. As more and more actors in the industry start to use it, it becomes important to better understand this framework to make the better use of it.

It is important to note, that while ECS is considered a great programming framework, most of the game that use it do not exclusively use it. Consequently, object oriented-programming might still be use in a lot of those projects.

Software engineering has developed a great amount of methods in object-oriented programing to make programs more maintenable. From video game specific artecture to video game specific design pattern. However, not as much work and research as been put into the different facet of ECS and how it truly compares to the industry-approved 

in this work, I shall focus on the maintenability of video games project focusing on ECS. As to really understand how maintenability specifically affect ECS, I had to find a way to know. With the overwhelming amount of video game project that are there it became obvious that simply comparing ECS project with other types of video game project would let me know how they rank. This study is intended as an initiation to see if the avergae ECS project is more maintenable than  other video game architecture.

# Related Work

Not much work as been done to observe the comportements in video games. However, BIRUK ASMARE MUSE and al. did a great job figuring what pattern led to the worst problems in video game developpement. This work lead the ground work on further empirical studies over video games, inlcuding this one. 

A couple a books and website, thus touch the subject of the ECS framework. One of the best to do so is raywenderlich. Of Course for those who knows unity DOTS technology, we know that unity also has its own devblog

# Methodology

This paper tries to better understand ECS project and the maintenability of such programs. To attain this effect,  I will use object oriented programing (OOP) as the baseline from which the ECS framework shall be compare. Since the industry has used OOP a lot, it will be easier to see what place ECS takes, and how it performs. my first research question being : 

RQ0. All ECS projects are base on object oriented projects.

To answer this question, I had to find a couple of repositories that used mostly or totally the ECS framework. To find the repositories, I search open-sourced project over Github with the key word "ECS". all project that did not have at least 100 commit were discarded as they were not mature enough to be considered. Some or all the ECS project would have a portion of the code written using another architecture. Therefore, to be considered, I manually check the project and made sure they were pluggins for well known engines or part of a core ECS engine of their own. Therfore this part was subjective. I decided that pluggins repositories would be considered as long as their architecture respected ECS with the same rules that any video game repositories were following (more than 100 commits). Since a manual verification was needed, only the 5 prefered projects were kept for comparison.

Then for further comprehension, a control group was needed. This controle group needed to not use ECS and be a well knoiw engine of the video game worlf. I simply used the video game key word for my search through github and than selected the top forked game engine, and all the open source game engine i found an ECS plugin for. I applied the same rules to find interesting repositories : they had to have at least 100 commits to be considered and I only kept the ones with the most commits. 

Once repository selection was completed, I looked on two different metric. First one will be the change-proness defined as the frequency of a file to be change. The conclusion we are trying to observe led to RQ1. 

RQ1. The average changeproness does not change in ECS projects from the average video game project.

To calculate this metric, we will look at the average amount of change a file from any project from its creation to its last version. Since longer projects will tend to have more changes but also more commit, this shall replresent fairly the changeproness.
equation : 

```
changeproness = TotalFileChanges / commits
```

To get find this information, I will use an automated approach that will count the presence of files in each commit of the projects. A file being present in a commit means it has been either created, modified (Changed) or destroyed. Than a simple ratio will tell me how much changes by files. We then will be able to find if the ratio of changes is higher or lower in ECS base projects. 

the second section will look at faultproness of files. this meant RQ2.

RQ2. The average faultproness does not change in ECS projects from the average video game project.

To make it simple, fault-proness is the amount of bug vreated in a program. However, since a lot of bug are not known, I needed to find a way to get most of the bug or at least the important ones. I used the commits that fixed bugs (the ones with the keyword bug or fix in) to get a fair estimate of the amount of bug in a programs. Knowing how many changes where intented to fix bug over the totral amount of change let us know a quick overview of how much effort was put into bug fixing over feature addition or modification. The smaller the ratio the less bugfix is needed per feature.

```
faultproness = TotalBugFixFilesChanges / TotalFileChanges
```

# Results

Finding the repositories was easier than anticipated since I had experience with a lot of different videogame engines and used quite my share of ECS based engine. Therefore, however subjective my analysis was, i was able to decern the true making of an ECS engine from the top  research prospect. I was mostly looking at an architecture that encouraged the usage of Components and Systems. That led me to 5 well known plugins that anyone who dwelved a bit into video game ECS development would know and that are presented in table 1. From those plugins, i diretly went and found the open source game engine linked to them. this led me to find GODOT engine. All the other game engine found were well known and had the most Fork. Fork made sense in the context of video game engines since the more fork were used, the more projects statrting with the engine there are. This enable to refute the null hypotheses RQ0. A lot of ECS engine does use a basic Object Oriented framework to work. The best example of which being godot ECS plugin. 

The sheer amount of commit every repository had made it so that an upper limit had to be drawn in order to enable me to finally get some results. For example, the principal godot repositories had over 53k commits. With the simple github API token given to me, I was only able to process 5k commits per hour. This would have resulted in over a day to get all the results from all the engines. Since I did not have the time to do all that, i decided to subsample. Instead, I focus on the most recent 500 commits of each repo. I was then able to find change proness of each repositories with the simple formula given at the start. Results are shown in the table 2. Flecs seems to be out of place with above of a million changes in the same commit. Since it seems to be anomalous data, it stops us from refuting our null hypothesis RQ1.

Last statistic that we wanted to see was faultproness. I used a naive approach that let me simply get the percentage of commits that focus on bugfixes out of the total amount of changes. This led to the percentage shown in table 3. Same as for table 2, flecs seems to be an anomalous data that does not bring clear information on the table. It has about 10 times more changes than the average repo, thus giving us a bad representation of ECS base code. Because of this, it is not possible to refute hypothesis RQ2.

# Discussion

As sad it was to find a strongly anomalous data, it is still possible to find something out of the remainder data. Consequently, we examine both godot repositorya nd it's ECS plugin godex. botrh had over 500 commits and can therefore be fairly well compare. Godex being newer and having less commit, it made sense for it to have the most changes by commit. around 1.7 times more changes. However, when looking at the most recents commits, and therfore at the ones who should try to tackle the most bug, we discover that fault seems to appear 1% less in godot. Entt is another great case study as it probably is the most known ECS engine on the open-source market, rivaled only by Unity DOTS technology. Seeing that over the 500 commits there were almost no bug and only feature addition or removal let us think that ECS might really be more maintenable. However, all these statistics seems to lack just a bit to prove a that ECS is also a more maintenable architecture than the other architecture used in video games. Form my perspective, it seems like changepronness (or at least my way of calculating it) does not seems to be affected by the architecture. However, althought impossible to acheive a clear conclusion, data does point toward fault-proness being a little bit smaller in ECS base architecture. the thing that blcks us from that conclusion is flecs results that gave us a whoping 50% fault ratio. 

This study needed to manually find the repositories that would be studied since there are no tools as far as i'm concern that let one knows if a repository is really of ECS architecture. Therefore, it limited my ability to find more data.We were able to prove that almost all ECS project does begin in some way, not as direct data-oriented programming, but in part as object oriented programming. It makes sense too, ass a lot of ecs engine/pluggins are made to work on well known video game architecture like Unity or Unreal Engine. 

# Validity

This research had validity issue that i tried to stop. First one being the fact that i am alone in my search. Howerver easier it might get, since i don't have to argue with anyone over wath i deem most important, it can also lead me to have focus on the wrong part or to not have considered every important aspect of the problem. It also led me to have subjective view that could not be challenge by collegues. To mitigate this issue, is tried to automate a lot of my technique. I focus on formulas that could give me the info i needed and would need subjectivity. 

For construct validity, it regards the tools used for this study. My main tool was github and its API. Since github is the biggest center for open source repositories it make sense to use it instead of any other. Also being alone, I had to focus my search where iot seemed to matter most and github is probably the place where i would grab the most informations.

for external validity, it regards how generalizable this study can be. With the way information was grabed,  this study is highly repoductible and used some big programs with above 2k commits to attain its objective. With that much commit to analyse, it make sense that the generalisation can be quite accurate. However, this study only focus on 5 repo from each due to resources reason.

# Conclusion

This study was aiming at 

# References

1. Gamma, E., Helm, R., Johnson, R.,, Vlissides, J. M. (1994). Design Patterns: Elements of Reusable Object-Oriented Software. Addison-Wesley Professional. ISBN: 0201633612

2. Ceruzzi, P. E. (2003). A history of modern computing. MIT press.

3. Wexelblat, R. L. (Ed.). (2014). History of programming languages. Academic Press.

4. Hansen, H., & Öhrström, O. (2020). Benchmarking and Analysis of Entity Referencing Within Open-Source Entity Component Systems.

5. Kafaji, K. (2018, March 29). Entity Component System in Unity: An Introduction. Ray Wenderlich. https://www.raywenderlich.com/847-entity-component-system-in-unity-an-introduction

6. Nystrom, R. (2014). Game Programming Patterns. Chapter 12: Entity Component System. Genever Benning. https://gameprogrammingpatterns.com/component.html

7. Stein, T. (2017, November 8). Introduction to Entity Component Systems. Gamasutra. https://www.gamasutra.com/blogs/TobiasStein/20171108/309451/Introduction_to_Entity_Component_Systems.php

8. ECSTY. (n.d.). Retrieved May 3, 2023, from https://ecsy.io/

9. Vittoria Nardone, Biruk Asmare Muse, Mouna Abidi, Foutse Khomh, and Massimiliano Di Penta. 2022. Video Game Bad Smells: What they are and how Developers Perceive Them. ACM Trans. Softw. Eng. Methodol. Just Accepted (September 2022). https://doi.org/10.1145/3563214
