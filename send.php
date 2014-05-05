<?php


/*
Test out some shell exec shite
*/
$find[] = 'â€œ'; // left side double smart quote
$find[] = 'â€'; // right side double smart quote
$find[] = 'â€˜'; // left side single smart quote
$find[] = 'â€™'; // right side single smart quote
$find[] = 'â€¦'; // elipsis
$find[] = 'â€”'; // em dash
$find[] = 'â€“'; // en dash
$find[] = '"'; //double quote

$replace[] = "'";
$replace[] = "'";
$replace[] = "'";
$replace[] = "'";
$replace[] = "...";
$replace[] = "-";
$replace[] = "-";
$replace[] = "'";


$bio = "Michael W. Abbott is a Los Angeles based Executive Producer, Producer and Director of Motion Pictures,Television, Branded Content & Commercials.

Abbott began his career at Savoy Pictures in Santa Monica as a Marketing Financial Analyst, overseeing P&A budgets ranging from $7M to $18M for the Company. During that time, Abbott produced the festival award winning music documentary on west coast rave culture, â€œSynergy: Visions of Vibe.â€  After departing from USA Broadcasting/Savoy Pictures in 1999, Abbott became Creative Executive at No
Prisoners Productions where in his personal time he co-created the Coachella Independent Film Festival housed in the critically acclaimed Coachella Music and Arts Festival.

In 2006, Abbott through TBWA/Chiat produced a hybrid documentary series â€œUNChartedâ€ for Apple on the global impact of the digital music revolution which shot in six countries over 3 months and featured over 170 hours of original content. During that time, Abbott was also a producer on â€œMy Name Isâ€¦â€ a festival award
winning scripted short film by Don Handfield, which was made eligible for a 2006 Academy Award.

Abbott followed up â€œMy Name Isâ€¦â€ as an Associate Producer on â€œExpiredâ€, the critically praised motion picture starring Samantha Morton, Jason Patric and Teri Garr, which premiered in and was sold at the 2007 Sundance Film Festival and competed in the 2007 Cannes Film Festival.

Between 2007-2008, Abbott produced, co-wrote and shot the acclaimed MyCadillacStory.com series for GM/Cadillac starring Jay Leno, Travis Barker and Tiki Barber to name a few. He shared directing duties on the Wynton Marsalis and Coach K MyCadillacStoryâ€™s, helping guide MyCadillacStory to become the 5th most
watched branded channel on YouTube for two years. 

Abbott also produced a series of high profile celebrity-driven online PSAs for U.S. Campaign for Burma, including a PSA starring Tila Tequila, which has been seen
over 12,000,000 times on YouTube alone. Abbottâ€™s viral PSA â€œThe Muzzler 2008â€ starring Jessica Alba succeeded with 550,000 Americans registering to vote online in 45 days.

In late 2009, Abbott produced and directed comedy commercials for SRS TruVolume and a multi-ad award winning online ad for Namco Bandaiâ€™s hit game Tekken 6 entitled â€œMotivation.â€

In 2009, Abbott along with EP Michael Shevloff created and sold â€œRunawayâ€, a docu-series that follows two young female Runaway Transport agents helping troubled teens off the streets, to MTV News & Docs. In 2010, Abbott and Shevloff sold their docu-series â€œBreaking Barriersâ€, which follows female F-18 jet fighter pilots in the
U.S. Navy, to Oprah Winfrey Network (OWN). In 2011, Abbott along with Trip Taylor (â€œJackassâ€) and Kyle Schember sold the animated television series â€œMeat Walletâ€ to Fuse Networks. Although two of the three series would shoot a pilot which Abbott actively Executive Produced, none would be picked up for series.

While shooting his TV pilots, Abbott would dive into producing a feature-length documentary â€œStripped: Greg Friedlerâ€™s Naked Las Vegasâ€, directed and co-produced by David Palmer (HIT & RUN). The film premiered on Showtime Networks on March 18th, 2010 and became one of the most watched documentaries in Showtime
Platform history for the network and TMC. Abbott followed up â€œStrippedâ€ as the Cinematographer of the documentary â€œAfter Porn Endsâ€ which became the #1 documentary on iTunes.

Abbott is currently in post production on the pilot for his reality anti-make-over series â€œBack In The Gameâ€ for NBCU/Esquire Network which he co-created and actively Executive Produced along with The Weiss Bros. and All3Media  (â€œUndercover Boss). He is currently in development  on the documentary THE WAR OF â€™84, which tells the incredible story of the U.S. menâ€™s Olympic boxing team at the 1984 Summer Olympic Games during the height of the Cold War.

A Los Angeles native, and son of Hollywood make up artist Larry Abbott, Michael attended the University of Southern Californiaâ€™s School of Cinema-Television with an emphasis on Critical Studies. He was honored twice with the Cinema-Television Schoolâ€™s Mary Pickford Award as well as with the Universityâ€™s Senior Recognition
Award upon graduation. ";


#$bio = "We are working on a 1-minute promotional video for an ad agency global network that will be initially be shown at a conference and later posted to a website. Concept and storyboard has been sold through, and we are looking to partner with someone to produce the video in After Effects. The video will contain a small amount of live action footage which is already shot. We will also supply the VO. We can supply the music if you'd like OR we can collaborate together on selecting the stock music. Los Angeles. ";

#$bio = "Nothing here.";

#pre-process quotes:
$bio = str_replace('"', "'", $bio);
$bio = str_replace($find, $replace, $bio);

#send to python:
$processed = shell_exec('python extract_industry_mentions.py "' . $bio . '"');

print $processed;

