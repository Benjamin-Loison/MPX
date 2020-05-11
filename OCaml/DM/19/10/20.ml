let calculer_peres racine fils freres =
	let peres = Array.make (Array.length fils) (-1) in
		let rec aux indice father =
			(*print_int indice;
			print_int father;
			print_newline(); linear*)
			let child = fils.(indice) and brother = freres.(indice) in
			if (child <> -1) then (peres.(child) <- indice; aux child indice); (* better ? *)
			if (brother <> -1) then (peres.(brother) <- father; aux brother father);
		in aux racine 0;
	peres;;

let test = Array.make 10 5;;

(* A1 *)

let racine = 4;;
let fils = [|-1; -1; -1; 0; 1; -1; 2|];;
let freres = [|-1; 6; 5; -1; -1; -1; 3|];;

calculer_peres racine fils freres;;

let rec aux freres indice = (*print_int indice; linear *)match freres.(indice) with
| (-1) -> 1
| f -> 1 + (aux freres f);;

let calculer_arites fils freres =
	let n = Array.length fils in
		let arites = Array.make n 0 in
			for i = 0 to (n - 1) do
				if (fils.(i) <> (-1)) then
					arites.(i) <- (aux freres fils.(i));
			done;
	arites;;

let calculer_arites fils freres =
	let rec aux indice = match freres.(indice) with
	| (-1) -> 1
	| f -> 1 + (aux f); in
	let n = Array.length fils in
		let arites = Array.make n 0 in
			for i = 0 to (n - 1) do
				if (fils.(i) <> (-1)) then
					arites.(i) <- (aux fils.(i));
			done;
	arites;;


calculer_arites fils freres;;

let i = ref 0;;

(* ne répond pas au problème car renvoie le tableau et ne modifie pas celui en argument *)
let inserer table nb d = (*incr i; print_int !i;*)
	let rec aux i j = match (i + j + 1) / 2 with
	| k when j < i -> Array.concat [(Array.sub table 0 k); [|d|]; (Array.sub table k ((Array.length table) - k))];
	| k when table.(k) > d -> aux (k + 1) j
	| k -> aux i (k - 1)
	in aux 0 nb;;

let inserer table nb d =
	let rec aux i j = match (i + j + 1) / 2 with
	| k when j < i ->
		for i = (max 0 (nb - 1)) to k do
			table.(i + 1) <- table.(i);
		done;
		table.(k) <- d;
	| k when table.(k) > d -> aux (k + 1) j
	| k -> aux i (k - 1)
	in aux 0 (nb - 1);
	nb + 1;;

5 / 2;; (* 2 *)

let a = [|1; 2|];;
let b = [|3; 4|];;
let b = Array.copy a;;
a;;
b;;

let table = [|3; 2; (-4); (-12)|];;
let nb = (Array.length table) - 1;;

let a = [|1; 2|];;
let b = [|4; 5|];;
let c = 3;;

Array.concat [a; [|c|]; b];;

Array.sub table 0 3;;
Array.sub table 1 3;;

table;;

inserer table nb 8;;
let nb = (Array.length table) - 1;;
inserer table nb 4;;
table;;
let nb = (Array.length table) - 1;;
inserer table nb 3;;
table;;
let nb = (Array.length table) - 1;;
inserer table nb 2;;
table;;
let nb = (Array.length table) - 1;;
inserer table nb 1;;
table;;
let nb = (Array.length table) - 1;;
inserer table nb (-3);;
table;;
let nb = (Array.length table) - 1;;
inserer table nb (-4);;
table;;
let nb = (Array.length table) - 1;;
inserer table nb (-7);;
table;;
let nb = (Array.length table) - 1;;
inserer table nb (-11);;
table;;
let nb = (Array.length table) - 1;;
inserer table nb (-12);;
table;;
let nb = (Array.length table) - 1;;
inserer table nb (-13);;
table;;
let nb = (Array.length table) - 1;;
inserer table nb (-17);;
table;;

table;;

table.(-1);; (* nop :'( *)

let print_array array =
	for i = 0 to ((Array.length array) - 1) do
		print_int array.(i); print_char ' ';
	done;;

(* ne répond pas au problème car utilise inserer qui n'y répond pas *)
(* cal peres et arites first and then cal tableau feuilles arbre initial classés par décroissance *)
(* puis codage Prüfer*)
(* better way ? *)
(* n ** 3 here and more precisely ? *)
let calculer_Prufer racine fils freres =
	let n = (Array.length fils) - 1 in
		let prufer = Array.make n 0
			and peres = calculer_peres racine fils freres
			and arites = calculer_arites fils freres in
		for i = 0 to (n - 1) do
			let feuilles = ref [||] and l = ref (-1) in (* in is important !!!!!! *)
			for j = 0 to n do
				if arites.(j) = 0 then
					(feuilles := inserer (!feuilles) !l j; incr l) (* use of nb ? *)
			done;
			let minFeuille = (!feuilles).(!l) in
			arites.(minFeuille) <- (-1);
			let father = peres.(minFeuille) in
			prufer.(i) <- father;
			arites.(father) <- arites.(father) - 1;
		done;
	prufer;;

(* corrigé DocSolus: *)

let inserer table nb d =
	let rec insere_pos pos =
		if pos >= 0 && table.(pos) < d then
		(	table.(pos + 1) <- table.(pos);
			insere_pos (pos - 1); )
		else
			table.(pos + 1) <- d
		in insere_pos (nb - 1);
		nb + 1;;

let calculer_Prufer racine fils freres =
	let n = Array.length fils and
		peres = calculer_peres racine fils freres and
		arites = calculer_arites fils freres and
		feuillesIndex = ref 0 in
	let feuilles = Array.make n 0 and prufer = Array.make (n - 1) 0 in
	for i = n - 1 downto 0 do
		if arites.(i) = 0 then
		(	feuilles.(!feuillesIndex) <- i;
			incr feuillesIndex)
	done;
	for i = 0 to n - 2 do
		let noeud = feuilles.(!feuillesIndex - 1) in
		let pere = peres.(noeud) in
			decr feuillesIndex;
			prufer.(i) <- pere;
			arites.(pere) <- arites.(pere) - 1;
			if arites.(pere) = 0 then
				feuillesIndex := inserer feuilles !feuillesIndex pere;
	done;
	prufer;;

(* A3 *)

let racine = 3;;
let fils = [|-1; 2; -1; 1; -1; -1; 4; 5; -1; 0; -1|];;
let freres = [|7; 9; 6; -1; -1; 8; -1; 10; -1; -1; -1|];;
calculer_peres racine fils freres;;
calculer_arites fils freres;;

calculer_Prufer racine fils freres;;
+
(* A1 *)

let racine = 4;;
let fils = [|-1; -1; -1; 0; 1; -1; 2|];;
let freres = [|-1; 6; 5; -1; -1; -1; 3|];;
calculer_peres racine fils freres;;
calculer_arites fils freres;;

calculer_Prufer racine fils freres;;

(* A2 *)

let racine = 1;;
let fils = [|-1; 0; 4; -1; -1; -1; 5|];;
let freres = [|2; -1; 6; -1; 3; -1; -1|];;

calculer_peres racine fils freres;;
calculer_arites fils freres;;

calculer_Prufer racine fils freres;;

let test n =
	for i = 0 to n do
		let i = 42 in
		();
	done;;

(* nb d'arites de n = nb d'occurence de n dans Prüfer *)
(* explication ? *)

let calculer_arites_par_Prufer prufer =
	let n = Array.length prufer in
	let arites = Array.make (n + 1) 0 in (* d'où ce décalage ? *)
	for i = 0 to n - 1 do
		print_int i;
		let j = prufer.(i) in
		arites.(j) <- arites.(j) + 1
	done;
	arites;;

let prufer = calculer_Prufer racine fils freres;;
calculer_arites_par_Prufer prufer;; (* works for three trees *)

let calculer_arbre prufer fils freres =
	let arites = calculer_arites_par_Prufer prufer and
		n = Array.length fils and
		feuilleIndex = ref 0 in
	for i = 0 to n - 1 do
		fils.(i) <- -1;
		freres.(i) <- -1;
	done;
	
	let feuilles = Array.make n 0 in
	for i = n - 1 downto 0 do
		if arites.(i) = 0 then
			feuilles.(!feuilleIndex) <- i;
			incr feuilleIndex;
	done;
	
	for i = 0 to n - 2 do
		let enfant = feuilles.(!feuilleIndex - 1) and
			pere = prufer.(i) in
			freres.(enfant) <- fils.(pere);
			fils.(pere) <- enfant;
			decr feuilleIndex;
			
			arites.(pere) <- arites.(pere) - 1;
			if arites.(pere) = 0 then
				feuilleIndex := inserer feuilles !feuilleIndex pere
	done;
	if n > 1 then prufer.(n - 2) else 0;;

(* A2 *)

let racine = 1;;
let fils = [|-1; 0; 4; -1; -1; -1; 5|];;
let freres = [|2; -1; 6; -1; 3; -1; -1|];;
let prufer = calculer_Prufer racine fils freres;;

let prufer = [|1|];;
let fils = [|-1|];;
let freres = [|-1|];;

calculer_arbre prufer fils freres;;

(* multiple ? *)

fils;;
freres;;