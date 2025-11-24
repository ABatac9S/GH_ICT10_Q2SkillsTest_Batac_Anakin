from pyscript import window

clubs = {
    "Anime Appreciation Society": {
        "Description": "A group dedicated to watching, discussing, and celebrating anime from every genre.",
        "Meeting Time": "Friday • 4:15 PM – 6:00 PM",
        "Location": "AV Room 2",
        "Moderator": "Ms. Hoshino",
        "Members": 34
    },
    "Retro Gaming League": {
        "Description": "Fans of classic consoles gather to play and talk about pixel art, OSTs, and gaming history.",
        "Meeting Time": "Wednesday • 3:30 PM – 5:00 PM",
        "Location": "Tech Lab",
        "Moderator": "Mr. Rintaro",
        "Members": 18
    },
    "Comic & Manga Circle": {
        "Description": "Readers and collectors unite to share their favorite manga volumes, comics, and graphic novels.",
        "Meeting Time": "Monday • 4:00 PM – 5:30 PM",
        "Location": "Library Annex",
        "Moderator": "Ms. Waguri",
        "Members": 26
    },
    "Animation & Storyboard Workshop": {
        "Description": "A hands-on club for students interested in character design, storyboarding, and 2D animation.",
        "Meeting Time": "Thursday • 4:10 PM – 5:40 PM",
        "Location": "Art Studio B",
        "Moderator": "Mr. Haru",
        "Members": 22
    }
}

def show_info(event=None):
    selected = window.document.getElementById("clubSelect").value
    club = clubs[selected]

    text = f"""
    <h2 class="club-title">{selected}</h2>

    <p><strong>Description:</strong> {club["Description"]}</p>
    <p><strong>Meeting Time:</strong> {club["Meeting Time"]}</p>
    <p><strong>Location:</strong> {club["Location"]}</p>
    <p><strong>Moderator:</strong> {club["Moderator"]}</p>
    <p><strong>Members:</strong> {club["Members"]}</p>
    """

    output = window.document.getElementById("output")
    output.innerHTML = text