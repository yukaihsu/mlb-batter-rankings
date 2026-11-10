import csv

class Batter:
    def __init__(self,Name,Team,Rank_preseason,AB,H,HR,BB,SF,TB):
        self.Name = Name
        self.Team = Team
        self.Rank_preseason = int(Rank_preseason)
        self.AB = int(AB)
        self.H = int(H)
        self.HR = int(HR)
        self.BB = int(BB)
        self.SF = int(SF)
        self.TB = int(TB)

    
    def avg(self):
        return self.H/ self.AB
    
    def obp(self):
        PA = self.AB + self.BB + self.SF
        return (self.H +self.BB)/ PA
    
    def slg(self):
        return self.TB/ self.AB
    
    def ops(self):
        return self.obp() + self.slg()
    
def load_batters(path= "batter_sate.csv"):
    batters = []
    with open(path, newline='', encoding='utf-8')as f:
        reader = csv.DictReader(f, skipinitialspace=True)
        for row in reader:
            clean ={}
            for k, v in row.items():
                key = k.lstrip("\ufeff").strip()
                clean[key] = v
            batters.append(Batter(
                Name= clean["Name"],
                Team = clean["Team"],
                Rank_preseason=clean["Rank_preseason"],
                AB=clean["AB"],
                H=clean["H"],
                HR=clean["HR"],
                BB=clean["BB"],
                SF=clean["SF"],
                TB=clean["TB"],
            ))
    return batters

def rank_batters(batters, metric="OPS", top_n= 20):
    metric = metric.upper()
    fn_map = {
        "AVG": Batter.avg,
        "OBP": Batter.obp,
        "SLG": Batter.slg,
        "OPS": Batter.ops
    }
    fn = fn_map.get(metric)
    if not fn:
        print("Not Valid")
        return [],[]
    
    rank = sorted(batters, key= lambda b: fn(b), reverse=True)
    return rank[:top_n], rank

def progress_table(batters, metric="OPS"):
    result = rank_batters(batters, metric, top_n=100)
    ranked = result[1] if isinstance(result, tuple) else result
    if isinstance(ranked[0], list):
        ranked = ranked[0]

    current_pos = {b.Name:i + 1 for i, b in enumerate(ranked)}

    improved, regressed, tied= [], [], []

    for b in batters:
        if b.Name in current_pos:
            delta =b.Rank_preseason - current_pos[b.Name]
            if delta > 0:
                improved.append((b, current_pos[b.Name],delta))
            elif delta < 0:
                regressed.append((b, current_pos[b.Name], delta))
            else:
                tied.append((b, current_pos[b.Name], 0))

    improved.sort(key= lambda x: x[2], reverse=True)
    regressed.sort(key= lambda x: x[2])
    tied.sort(key= lambda x: x[1])
    return improved, regressed, tied
