# TC: O(m*n)
# SC: O(m*n)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        self.color = color
        
        self.m = len(image)
        self.n = len(image[0])
        
        self.initial = image[sr][sc]
        
        self.dirs = [[1,0], [0,1], [-1,0], [0,-1]]
        self.dfs(image, sr, sc)
        return image
    
    def dfs(self, image, sr, sc):
        
        # base condition
        if sr < 0 or sr == self.m or sc < 0 or sc == self.n or image[sr][sc] != self.initial:
            return
        
        image[sr][sc] = self.color
        
        # recursive condition
        for x,y in self.dirs:
            self.dfs(image, sr+x, sc+y)

            
        
        