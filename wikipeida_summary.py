import wikipedia
def fetch_summary():
    topic = input("Enter a topic to search on Wikipedia: ")
    try:
        #change the value of the {sentences} to get brief or long summary
        summary = wikipedia.summary(topic, sentences=15)
        print("\n📚 Wikipedia Summary:")
        print(summary)
    except wikipedia.exceptions.DisambiguationError as e:
        print("\n⚠️ Too many results. Be more specific. Options include:")
        for option in e.options[:5]:  # Show only top 5 options
            print(" -", option)
    except wikipedia.exceptions.PageError:
        print("\n❌ No page found for that topic.")
    except Exception as e:
        print(f"\n🚨 An error occurred: {e}")
fetch_summary()
