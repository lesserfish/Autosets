<script>
	// Imports
	import Introduction from "./Components/Introduction.svelte"
	import Template from "./Components/Template.svelte"
	import Output from "./Components/Output.svelte"
	import Load from "./Components/Load.svelte"
	import { fade, fly } from 'svelte/transition';

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

	let animationDelay = 200;
	let animationSpeed = 600;

</script>
<body class="bg-white">
<Load bind:AppObjects={AppObjects}/>


<div class ="container-fluid shadow">
	<div class="row">
	<nav class="navbar sticky-top navbar-light">
		<div class="container NavbarContainer ">
			<div class="navbar-brand">
				<h1 class="display-6 text-dark">AUTO <span class="text-primary">SETS</span></h1>
			</div>
		</div>
	</nav>
	</div>
</div>

<div class="container Main">
	<div class="row">
		<div class="col">
			<button type="button" class="btn btn-outline-primary shadow-sm {mode == 0 ? "disabled" : ""}" on:click={() => { mode = Math.max(mode - 1, 0); animationSpeed = -1 * Math.abs(animationSpeed);} }> Previous Step </button> 
		</div>
		<div class="col-6"></div>	
		<div class="col">
			<button type="button" class="btn btn-outline-primary shadow-sm {mode == 2 ? "disabled" : ""}" on:click={() => { mode = Math.min(mode + 1, 2); animationSpeed = Math.abs(animationSpeed); }}> Next Step</button> 
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

		<nav class="navbar fixed-bottom navbar-light">
			<div class="col-12">
				<div class="navbar-text text-center">
					{#if mode==0}
					
					<div in:fly="{{ x: animationSpeed, duration: animationDelay, delay: animationDelay}}"><h5>Hello there!</h5></div>
					{:else if mode == 1}
					<div in:fly="{{ x: animationSpeed, duration: animationDelay, delay: animationDelay}}"><h5>Woah!</h5></div>
					{:else}
					<div in:fly="{{ x: animationSpeed, duration: animationDelay, delay: animationDelay}}"><h5>Good god...</h5></div>
					{/if}
				</div>
			</div>
		</nav>
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
	.NavbarContainer{
		margin-left:2%
	}
</style>