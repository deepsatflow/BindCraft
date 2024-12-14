TIMEOUT=1400 GPU=A100 modal run --detach modal_bindcraft.py --input-pdb 6aru_final_chain_A_domain_3.pdb --target-hotspot-residues A356,A440-441 --lengths 142,142  --number-of-final-designs 1
TIMEOUT=1400 GPU=A100 modal run --detach modal_bindcraft.py --input-pdb 6aru_final_chain_A_domain_3.pdb --target-hotspot-residues A356,A440-441 --lengths 142,142 --number-of-final-designs 1 --design-protocol-path default_4stage_multimer_rg.json

