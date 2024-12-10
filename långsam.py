def txt(text):
    import time
    import sys
    mening = ""


    for x in text:
        mening += x
        print(mening, end='\r')
        sys.stdout.flush()
        time.sleep(.06)


#text = "Model weights for the first version of Llama were made available to the research community under a non-commercial license, and access was granted on a case-by-case basis"

