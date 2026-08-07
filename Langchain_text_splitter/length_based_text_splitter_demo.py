from langchain_text_splitters import CharacterTextSplitter

text = """
Morning brings a fresh start to every living thing. The dark night fades away as soft gold light touches the ground. Leaves move gently in a quiet breeze. Small animals wake up and start to look for food. Flowers open their petals to catch the warm sun. This quiet time feels very calm. People can take a deep breath and feel the clean air. It is a good hour to think about new goals and plans for the day ahead.
When noon arrives, the world is full of life and noise. Bright light covers every field and street. Bees fly from plant to plant to collect sweet nectar. Green leaves make food using the bright rays above. Workers move about their daily tasks with busy hands. Rivers flow fast over smooth stones. Nature works hard during these bright hours. Even with all this motion, a person can still find a shady spot under a big tree to rest and watch the clouds float by.
As afternoon ends, the bright day shifts into a cool evening. The sun moves down near the western horizon. The sky paints itself in shades of orange, pink, and deep purple. Shadows grow long across the open fields. Birds fly back to their nests in the high branches. The loud noises of the day grow soft and quiet. Crickets begin their night songs in the tall grass. This transition time reminds everyone that rest is just as important as work.
Night brings deep quiet to the land. A silver moon rises to guide the dark hours. Stars blink like tiny lights in a vast cosmic sea. Most creatures stop their movement and fall fast asleep. The cool night air feels soft on the skin. It is a time for deep rest and quiet dreams. When the morning comes again, the great wheel of nature will turn once more, bringing life back to the waiting world.
"""

# create the object of text-splitter.
splitter = CharacterTextSplitter(
    chunk_size = 100, 
    chunk_overlap = 10, 
    separator = ''
)

# create the chunks.
chunks = splitter.split_text(text)

# print the chunnks
print(chunks)
