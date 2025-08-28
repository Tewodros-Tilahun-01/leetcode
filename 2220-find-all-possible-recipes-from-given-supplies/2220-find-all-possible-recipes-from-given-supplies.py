class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        sup = set(supplies)
        graph = collections.defaultdict(list)
        incoming = collections.defaultdict(int)
        queue = collections.deque(supplies)
        toposort = []
        for i in range(len(recipes)):
            for j in ingredients[i]:
                if recipes[i] not in sup:
                    graph[j].append(recipes[i])
                    incoming[recipes[i]] += 1        
        while queue:
            ig = queue.popleft()
            for recipe in graph[ig]:
                incoming[recipe] -= 1
                if incoming[recipe] == 0:
                    toposort.append(recipe)
                    queue.append(recipe)
        return toposort
        