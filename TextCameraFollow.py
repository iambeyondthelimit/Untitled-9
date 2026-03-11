from CodeVideoRenderer import * #pip install CodeVideoRenderer

video = CameraFollowCursorCV(
    code_string="""
print(\"\"\"
    To the bone by pamungkas
    Of all the ones that begged to stay
    I'm still longing for you
    Of all the ones that cried their way
    I'm still waiting on you
    Maybe we seek for something that
    We couldn't ever have
    Maybe we choose the only love
    We know we won't accept
    Or maybe we're taking all the risks
    For something that is real
    Cause maybe the greatest love of all
    Is who the eyes can't see yeah
    print("Made by KAJ)\"\"\")"""
    ,  #this is just an example. lyrics from to the bone by pamungkas
    
    language="python"
)

video.render()
