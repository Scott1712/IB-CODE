text = "$$$ALERT###now_contact=>dr_strange42@multiverse.mcu!!!__important__^quick~resend% ASAP>>>>primary:   anna.karenina@literature.ru<<<;(backup?)~~contact_me@protonmail.ch//over&out;; secondary_email***==>   lee.jordan_broadcast@hogwarts.ac.uk%%username==ghost&&haunter_99@phantom.zone##!USE_IMMEDIATELY!!! alt=>>||gamma-ray@cosmic-ray.nasa.gov<<|random-blip>>>__click-here__ for details:::: woo_woo@crazy-train.ioNOTE!!==martin.king@civilrights.org<<====help.line:: active.support@responder.help.com@@REBOOT SYSTEM---error404@unknown.tld___;   DEBUG=trace.trace@deep.stack.dev!reach-out @@@ ninja47@dojo.hidden.jp >>> send ++++ retry: fail-safe@secure-mail.systems!!Update#####user.test@staging-env.qa.xyz<<<::ignore_thiscontact-> harry_potter777@owlpost.magic.uk,  extra:: hogsmeade.connection@wizards.edu@new#priority==>> urgent_matter@redflag.alert.net <<---CONFIRM NOW!!(###randomized-junk-data###)==>[xray_echo_14@aviator.mail.plane]<<<inflight_data%%keep-moving##MEGAIMPORT::SENDER??::jon_snow@thewall.watch.north!!!winter-coming!memo_to: bilbo.baggins@shire.middleearth.hobbit  //for-review--pleasehidden!user! detected~~ alpha_beta@hidden.zone.underground###MASKED###   redirect_to= phoenix.down@revive.org ->>> alt.access@backup-plan.io##!RUN.run.run@forest.gump.movie~~life.box@@chocolatesextra_security:: two_factor@auth.system.safe!!---retry loginnotify_admin===overwatch.alerts@blizzard.games || tracer_london@heroes.uk.eu(END-OF-LINE?)# kevin_flynn@grid.encom.io [TRON MODE] ::data_stream::activeurgent_upload>>whoami@cyber.space@data-overload__jacked.in__[]"
clean = text.replace("!"," ").replace("£"," ",).replace("$"," ").replace("%"," ").replace("^"," ").replace("&"," ").replace("*"," ").replace("&"," ").replace("*"," ").replace("("," ").replace(")"," ").replace("="," ",).replace("+"," ").replace("["," ").replace("]"," ").replace("{"," ").replace("}"," ").replace(";"," ").replace(":"," ").replace("#"," ").replace("~"," ").replace("<"," ",).replace(">"," ").replace("'"," ").replace("/"," ").replace("?"," ").replace("`"," ").replace("¬"," ").replace("---"," ").replace("|"," ").replace("@@@"," ").replace("__"," ")
words = clean.split(" ")

for i in range(0,5):
    print(" ")
print("Clean list below")
for word in words:
    willPrint = False
    for i in range(0,len(word)):
        if word[i] == "@":
            willPrint = True
    if willPrint == True:
        print(word)