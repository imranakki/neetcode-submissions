class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map<int, int> m;
        for(auto &e:nums){
            if(m[e] == 1){
                return true;
            }
            m[e]++;
        }
        return false;
    }
};
