# spacy_pipes.py
from nlpia2.spacy_language_model import load
import pandas as pd


if __name__ == '__main__':
    lines = [
        'Gebru had determined that publishing research papers was more effective at bringing forth the ethical change she was focused on than pressing her superiors in the company.',
        'She and five others coauthored a research paper: "On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?"'
        ]
    text = lines[0]
    nlp_coref = load('en_coreference_web_trf')
    doc_coref = nlp_coref(text)
    print(doc_coref.spans)
    
    nlp = load('en_core_web_lg')
    doc = nlp(text)
    
    tags = []
    for t in doc:
        tags.append(
            dict(Token=t.text, POS=t.pos_, Dependant=t.dep_,
                 OOV=t.is_oov,
                 Entity=t.ent_type_))
    df = pd.DataFrame(tags)
    print(df)

    print(list(doc.sents))