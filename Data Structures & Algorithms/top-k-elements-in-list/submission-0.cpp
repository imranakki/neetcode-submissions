class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> m;
        for(auto &e:nums) m[e]++;
        int n = nums.size();
        vector<vector<int>> cnt(n + 1);
        for(auto &[x, y]:m) cnt[y].push_back(x);
        vector<int> ans;
        for(int i = n; i >= 0; i--){
            for(auto &e:cnt[i]){
                if(k == 0) break;
                ans.push_back(e);
                k--;
            }
            if(k == 0) break;
        }
        return ans;
    }
};
