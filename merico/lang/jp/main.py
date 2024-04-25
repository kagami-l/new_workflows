import sys
from lib.util.openai import create_chat_completion_chunks


def main(sentence: str) -> str:
    print(f"\n\nWill translate the sentence to Japanese.\n\n")

    chunks = create_chat_completion_chunks(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Translate this sentence to Japanese: \n\n{sentence}\n\n"}],
        temperature=0.1,
    )
    for chunk in chunks:
        if chunk.choices[0].finish_reason == "stop":
            break

        content = chunk.choices[0].delta.content
        if content is not None:
            print(content, flush=True, end="")


if __name__ == "__main__":
    main(sys.argv[1])