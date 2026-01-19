class chai_utils:

    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]


raw = " tea leaves    ,  milk        ,   sugar  ,              ginger "

print(raw)

clean = chai_utils.clean_ingredients(raw)

print(clean)

