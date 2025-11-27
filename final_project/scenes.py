from classes import Scene, Choice

    scene1 = Scene(
        "approach_kyoto",
        '''The Road from Arashiyama glows orange ahead...
        The onsen were lovely, don't you think?" okāsan asked.
        And it had been. The hot springs had revitalized my spirits
        and I was eager to return home. After a quiet retreat
        to the neighboring Arashiyama, I seemed to be the only one among us
        who felt that way. How easy life could have been if we had stayed forever...
    ''' 
        ,
        [], 
        auto_next="togetsukyo_bridge"
    )

    scene2 = Scene(
        "togetsukyo_bridge",
        "The Road from Arashiyama glows orange ahead...",
        [
            Choice("1", "Hurry toward the city.", "closer_to_city"),
            Choice("2", "Check on your sibling.", "check_sibling")
        ]
    )

scenes = {
    "approach_kyoto": scene1,
    "togetsukyo_bridge": scene2,
}
