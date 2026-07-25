class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> ms, mt;
        for(auto &e:s) ms[e]++;
        for(auto &e:t) mt[e]++;
        return ms == mt;
    }
};
