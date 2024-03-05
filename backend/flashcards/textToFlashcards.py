import openai
from config import Config
from dataclasses import dataclass

api_key = Config().API_KEY

openai.api_key = api_key
sample_info = "Cristiano Ronaldo dos Santos Aveiro GOIH ComM (Portuguese pronunciation: [kɾiʃˈtjɐnu ʁɔˈnaldu]; born 5 February 1985) is a Portuguese professional footballer who plays as a forward for and captains both Saudi Pro League club Al Nassr and the Portugal national team. Widely regarded as one of the greatest players of all-time, Ronaldo has won five Ballon d'Or awards,[note 3] a record three UEFA Men's Player of the Year Awards, and four European Golden Shoes, the most by a European player. Kaamya does not like coffe. Kristoffer does like coffee. "


def request_chat_completion(role: str = "system", message: str = "") -> list[str]: 
    """
    Returns a response from the OpenAI API

    Args:
        previous_message (dict): The previous message in the conversation
        role (str, optional): The role of the message. Defaults to "system".
        message (str, optional): The message to be sent. Defaults to "".
        functions (list, optional): The functions to be used. Defaults to [].
    
    Returns:
        response list[str]: The response from the OpenAI API
        if empty string, an error has occured
    """
    result = ""
    if message == "":
        result = "Error: No message provided"
    else:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": role, "content": message}
            ]
        )
        result = response.choices[0].message.content
    return result
    
def generate_template(sample_info: str = sample_info) -> str:
    """
    Returns a template with the correct flashcard and prompt format which can be used to generate flashcards using the sample text
    """

    example = f"Front: Which year was the person born? - Back: 1999 | Front: At what temperture does water boil? - Back: 100 degrees celsius | Front: MAC - Back: Message Authentication Code"
    template = f"Create a set of flashcards using the following format: {example} from the following text: {sample_info}. Use only information from the text to generate the flashcards. Use only the given format. DO not use line breaks. Do not use any other format"

    return template

def generate_flashcards(sample_info: str = sample_info) -> list[str]:
    """
    Returns a flashcard generated from the sample text

    Args:
        sample_info (str): The sample text to be used

    Returns:
        list: The list of flashcards generated from the sample text
    """
    # TODO: Create this function
    template = generate_template(sample_info)
    response = request_chat_completion("system", message=template)
    response = response.split("|")
    return response

@dataclass
class Flashcard:
    front: str
    back: str

def parse_flashcard(flashcards_data: list[str]) -> list[Flashcard]:
    """
    Returns a list of the Flashcard dataclass 

    Args:
        flashcards_data (list[str]): The flashcard to be parsed

    Returns:
        list[Flashcard]: A list of Flashcards with the front and back of the flashcard

    example:
        [Flashcard(front="apple", back="banana"), Flashcard(front="orange", back="grape")]

    """
    # TODO: Create this function
    flashcards = []

    for i in flashcards_data:
        i = i.replace("Front: ", "").replace("Back: ", "")
        i = i.split("-")
        flashcards.append(Flashcard(front=i[0].strip(), back=i[1].strip()))
    
    return flashcards

def parse_for_anki(flashcards: list[Flashcard]) -> str:
    """
    Returns a string with the flashcards in the correct format for Anki

    Correct format: front:back
    Example: "apple:"banana"

    Args:
        flashcards (list[Flashcard]): The flashcards to be parsed

    Returns:
        str: A string with the flashcards in the correct format for Anki
    """
    # TODO: Create this function
    pass


def generate_parsed_flashcards(sample_info: str = sample_info) -> list[dict[str, str]]:
    """
    Returns a list of dictionaries with the front and back of the flashcard

    Args:
        sample_info (str): The sample text to be used

    Returns:
        list[dict[str, str]]: A list of dictionaries with the front and back of the flashcard
    """
    flashcards = generate_flashcards(sample_info)
    return parse_flashcard(flashcards)