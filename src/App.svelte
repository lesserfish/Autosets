<script>
	// Imports
	import Introduction from "./Components/Introduction.svelte"
	import Template from "./Components/Template.svelte"
	import Output from "./Components/Output.svelte"
	import Load from "./Components/Load.svelte"
	import { fly } from 'svelte/transition';

	// File loads
	let AppObjects = {
		workoutObject : [],
		muscleGroupArray : [],
		exerciseTypeArray : [],
		equipmentArray : [],
		experienceArray : [],
	};

	// Local variables
	let mode = 0;
	let value = 0;

	let animationDelay = 200
	let animationSpeed = 600

</script>
<body class="bg-white">
<Load bind:AppObjects={AppObjects}/>


<div class ="container-fluid shadow">
	<div class="row">
	<nav class="navbar sticky-top navbar-light">
		<div class="container Navbar">
			<a class="navbar-brand" href="#">
				<h1 class="display-6 text-dark">Autosets </h1>
			</a>
		</div>
	</nav>
	</div>
</div>

<div class="container Main">
	<div class="row">
		<div class="col">
			<button type="button" class="btn btn-light" on:click={() => { mode = Math.max(mode - 1, 0); animationSpeed = -1 * Math.abs(animationSpeed);} }> Previous Step </button> 
		</div>
		<div class="col-6"></div>	
		<div class="col">
			<button type="button" class="btn btn-light" on:click={() => { mode = Math.min(mode + 1, 2); animationSpeed = Math.abs(animationSpeed); }}> Next Step</button> 
		</div>
	</div>
	<div class="Component">
		{#if mode == 0}
			<div in:fly="{{ x: animationSpeed, duration: animationDelay, delay: animationDelay}}" out:fly="{{ x: -1 * animationSpeed, duration: animationDelay}}"> 
				<p>Hello</p>
				<Introduction />-->
			</div>
			
		{:else if mode == 1}
			<div in:fly="{{ x: animationSpeed, duration: animationDelay, delay: animationDelay}}" out:fly="{{ x: -1 * animationSpeed, duration: animationDelay}}"> 
				<p>This is a</p>
				<Template bind:value={value}/>			
			</div>
		{:else}
			<div in:fly="{{ x: animationSpeed, duration: animationDelay, delay: animationDelay}}" out:fly="{{ x: -1 * animationSpeed, duration: animationDelay}}"> 
				<p> Test</p>
				<Output bind:value={value}/>
			</div>

	{/if}	
	</div>

	<div class="Footer"></div>
</div>
</body>
<style>
	body{
		max-width: 100%;
		overflow-x: hidden;
	}
	.Main{
		text-align: center;
		padding: 2%;
	}
	.Navbar{
		margin-left:2%
	}
</style>