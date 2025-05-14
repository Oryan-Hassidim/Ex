names = {"Noa", "Dorit", "Galit", "Or", "Michal", "Tal"}

way = {"bus": None,
       "foot": None,
       "private": None,
       "korkinet": None,
       "bike": None,
       "train": "Noa"}

work = {"Dev-Ops": None,
        "Data-Scientist": None,
        "QA": None,
        "ML": None,
        "Back-End": None,
        "Front-End": None}

changes = [None for _ in range(945, 951)]

order = [None for _ in range(1, 7)]


def equals(l1, l2):
    return (all((n is None or None in l2 or n in l2) for n in l1)
            and all((n is None or None in l1 or n in l1) for n in l2))

# criteria


def criteria():
    # 1
    t = {"Noa", work["Dev-Ops"], way["foot"]}
    yield order[-1] is None or order[-1] not in t
    yield equals(changes[0:3], t)
    # 2
    t = {way["private"], work["Data-Scientist"], "Dorit"}
    yield order[0] is None or order[0] not in t
    yield equals(changes[3:6], t)
    # 3
    t = {work["QA"], "Galit", way["korkinet"]}
    yield equals(order[0:3], t)
    yield changes[-1] is None or changes[-1] not in t
    if "Or" in order:
        yield all(changes.index(n) < changes.index("Or")
                  for n in t
                  if n is not None and n in changes)
    # 4
    t = {way["bike"], "Michal", work["ML"]}
    yield equals(order[3:6], t)
    yield changes[0] is None or changes[0] not in t
    if "Tal" in order:
        yield all(changes.index(n) > changes.index("Tal")
                  for n in t
                  if n is not None and n in changes)
    # 5
    yield "Noa" not in changes[0::2]  # 0 <=> 945
    if "Noa" in changes and way["bike"] is not None and way["bike"] in changes:
        yield changes.index(way["bike"]) + 1 == changes.index("Noa")
    if "Noa" in changes and work["Back-End"] is not None and work["Back-End"] in changes:
        yield changes.index(work["Back-End"]) - 1 == changes.index("Noa")
    # 6
    yield work["Front-End"] != "Galit"
    if "Galit" in order and "Or" in order:
        yield order.index("Galit") < order.index("Or")
    if "Or" in order and work["Front-End"] is not None and work["Front-End"] in order:
        yield order.index("Or") < order.index(work["Front-End"])
    if work["Front-End"] is not None and work["Front-End"] in changes:
        changes.index(work["Front-End"]) in {2, 3}


def validate():
    return all(criteria())


def fill_changes():
    if not validate():
        return
    for i in range(len(changes)):
        if changes[i] is None:
            for n in names:
                if n not in changes:
                    changes[i] = n
                    yield from fill_changes()
                    changes[i] = None
    if None not in changes:
        yield {"way": way, "work": work, "changes": changes, "order": order}


def fill_order():
    if not validate():
        return
    for i in range(len(order)):
        if order[i] is None:
            for n in names:
                if n not in order:
                    order[i] = n
                    yield from fill_order()
                    order[i] = None
    if None not in order:
        yield from fill_changes()


def fill_work():
    if not validate():
        return
    for w in work:
        if work[w] is None:
            for n in names:
                if n not in work.values():
                    work[w] = n
                    yield from fill_work()
                    work[w] = None
    if None not in work.values():
        yield from fill_order()


def fill_way():
    if not validate():
        return
    for w in way:
        if way[w] is None:
            for n in names:
                if n not in way.values():
                    way[w] = n
                    yield from fill_way()
                    way[w] = None
    if None not in way.values():
        yield from fill_work()


for result in fill_way():
    print(result)
