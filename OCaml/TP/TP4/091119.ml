type tas = {mutable n : int; t : int array};;

(*Q1*)

let exemple = {n=6;t= Array.make 50 0};;			
exemple.t.(0) <- 5;;
exemple.t.(1) <- 4;;
exemple.t.(2) <- 3;;
exemple.t.(3) <- 2;;
exemple.t.(4) <- 1;;
exemple.t.(5) <- 0;;

exemple;;

(*Q2*)

let echange t i j = 
	let c = t.(i) in 
		t.(i) <- t.(j);
		t.(j) <- c;;

let rec monte t k = match k with 
	|0 -> ()
	|k -> let indice_pere = (k-1)/2 in 
		   if t.(indice_pere) < t.(k) then 
		   	 	(echange t indice_pere k;
		   		monte t indice_pere;);;

let rec descend t n k = match k with 
	|k when 2*k + 1 >= n -> ()
	|k -> let j = if 2*k+2 = n || t.(2*k+1) > t.(2*k+2)
		then 2*k+1
		else 2*k+2
		in if t.(k) < t.(j)
			then echange t k j; descend t n j;;

(*Q3*)

let extraire tas = 
	let racine = tas.t.(0) in 
	   tas.n <- tas.n - 1;
		echange tas.t 0 tas.n;
		descend tas.t tas.n 0; (* can't make a monter version ? *)
		racine;;

extraire exemple;;
exemple;;

(*Q4*)

(* O(log n) *)
let insertion tas x = 
	tas.t.(tas.n) <- x;
	monte tas.t tas.n;
	tas.n <- tas.n + 1;;

insertion exemple 6;;
exemple;;

(*Q5*)

let creation t =
	let l = Array.length t in
		for i = 0 to (l - 1) do
			monte t i
		done;
		{n=l; t=t};;

(* O(nlog n) *)			
(* teacher two methods *)
let creetas tab =
	let a = Array.make 50 0 in
	let n = Array.length tab in
	let res = {n = 0; t = a} in
	for i = 0 o n - 1 do
		insertion res tab.(i)
	done; res;;

let creetas_bis tab =
	let res = {n = Array.length tab; t = tab} in
	for i = 0 to (res.n - 1) do
		monte res i
	done;
	res;;

let heapsort tab =
	let t = creation tab in
	for i = 0 to (t.n - 1) do
		extraire t
	done;;

let tastest = creation [|0; 14; 10; 8; 7; 9; 3; 11; 12; 13|];;

not true;;

let pere i = (i - 1) / 2;;

let rec pair i =
	if i = 0 then true
	else not (pair (pere i));;

pair 0;;
pair 14;;
pair 10;;
pair 8;;
pair 7;;
pair 11;;

let rec descendants t i =
	let n = t.n in match i with
	| i when i > n - 1 -> []
	| i -> i::(descendants t.(2*i+1))@(descendants t.(2*i+2));;
	
let descendants t i = let n = t.n in
	let rec aux t i acc = match i with
	| i when i > n - 1 -> acc
	| i -> i::(aux t (2*i+1) (aux t (2*i+2) acc))
	in aux t i [];;

let mintas t = t.t.(0);;

let maxtas t =
	if t.n = 1 then t.t(0)
	else if t.n = 2 then
		t.t.(1) else
		max t.t.(1) t.t.(2);;

let verifie t =
	let n = t.n in
	let tas = t.t in
	let rec aux t i = match i with
	| i when 2 * i + 1 > n - 1 -> (tas.(i), tas.(i), true)
	| i when 2 * i + 1 = n - 1 -> if pair i then (tas.(i), tas.(2*i+1), tas.(i) < tas.(2 * i + 1))
	else (tas.(2 * i + 1), tas.(i), tas.(i) > tas.(2*i+1))
	| i -> let (ming, maxg, boolg) = aux t (2 * i + 1)
		and (mind, maxd, boold) = aux t (2 * i + 2) in
			if pair i then
				(tas.(i), max maxg maxd, boolg && boold &&
					tas.(i) < min ming mind)
			else
				(min ming mind, tas.(i), boolg && boold &&
					tas.(i) > max maxg maxd)
	in let (_, _, bool) = aux t 0 in bool;;

