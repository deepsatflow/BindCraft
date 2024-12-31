pdb_selchain -A target.pdb > target_A.pdb
pdb_tofasta -multi 6aru_final_chain_A_domain_3_l50_s590216_mpnn11_model1.pdb

# add summary command

pdb_wc hu_nano2_4_85252b_A.pdb

pdb_rplchain -A:C output.pdb | pdb_tidy | pdb_sort -C | pdb_tidy | pdb_rplchain -B:A | pdb_tidy | pdb_rplchain -C:B | pdb_tidy | pdb_reatom > final.pdb

pdb_rplchain -A:B hu_nano2_4_85252b_A.pdb | pdb_tidy > hu_nano2_4_85252b_B.pdb
pdb_merge 6aru_final_chain_A_domain_3.pdb hu_nano2_4_85252b_B.pdb > input.pdb
pdb_mkensemble 6aru_final_chain_A_domain_3.pdb hu_nano2_4_85252b_B.pdb > input.pdb

pdb_merge 6aru_final_chain_A_domain_3.pdb hu_nano2_4_85252b_B.pdb | pdb_tidy > input.pdb
