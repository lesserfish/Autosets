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

    class ExerciseEntry{
        constructor(MuscleGroups, ExerciseTypes, Equipments, Experience)
        {
            this.MuscleGroups = MuscleGroups;
            this.ExerciseTypes = ExerciseTypes;
            this.Equipments = Equipments;
            this.Experience = Experience;
        };
    };

    let a = new ExerciseEntry(["Abdomen, Upper Back, Lower Back, Pelvis"], ["Strength, Stretching"], ["Dumbbell, Bodyweight, Rope"], ["Beginner, Intermediate, Advanced"]);
    let b = new ExerciseEntry(["Upper Back, Lower Back, Pelvis, Buttocks"], ["Strength, Stretching, Powerlifting"], ["Dumbbell, Bodyweight"], ["Intermediate, Advanced"]);
    let TemplateList = [a, b];
	
	// Local variables
	let mode = 0;
	let value = 0;

	let animationDelay = 200;
	let animationSpeed = 600;


</script>
<body class="bg-white">

{#if mode==0}
	<div class="BackgroundImage imageA">
		<img src="/images/human_a.png" alt=""  
		in:fly="{{ x: animationSpeed, duration: animationDelay, delay: animationDelay}}"
		out:fade="{{ x: -1 * animationSpeed, duration: animationDelay}}">
	</div>
{:else if mode == 1}
	<div class="BackgroundImage imageB">
		<img src="/images/human_b.webp" alt=""
		in:fly="{{ x:  - 1 * animationSpeed, duration: animationDelay, delay: animationDelay}}"
		out:fade="{{ x:  animationSpeed, duration: animationDelay}}">
	</div>
{:else}	
	<div class="BackgroundImage imageC">
		<img src="/images/human_c.webp" alt=""
		in:fly="{{ x: animationSpeed, duration: animationDelay, delay: animationDelay}}"
		out:fade="{{ x: -1 * animationSpeed, duration: animationDelay}}">
	</div>
{/if}


<Load bind:AppObjects={AppObjects}/>


<div class ="container-fluid shadow">
	<div class="row">
	<nav class="navbar sticky-top navbar-light">
		<div class="container NavbarContainer ">
			<div class="navbar-brand">
				<h1 class="display-6 text-dark">AUTO <span class="text-secondary">SETS</span></h1>
			</div>
		</div>
	</nav>
	</div>
</div>

<div class="container Main">
	<div class="row">
		<div class="col">
			<button type="button" class="btn btn-outline-secondary shadow-sm {mode == 0 ? "disabled" : ""}" on:click={() => { mode = Math.max(mode - 1, 0); animationSpeed = -1 * Math.abs(animationSpeed);} }> Previous Step </button> 
		</div>
		<div class="col-6"></div>	
		<div class="col">
			<button type="button" class="btn btn-outline-secondary shadow-sm {mode == 2 ? "disabled" : ""}" on:click={() => { mode = Math.min(mode + 1, 2); animationSpeed = Math.abs(animationSpeed); }}> Next Step</button> 
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
				<Template bind:AppObjects={AppObjects} bind:TemplateList={TemplateList} />			
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
		overflow-y: hidden;
		z-index: 3;
	}
	.Main{
		text-align: center;
		padding: 2%;
	}
	.NavbarContainer{
		margin-left:2%
	}
	.BackgroundImage{
		position:absolute;
		overflow:hidden;
		z-index: 0;
		pointer-events: none;
	}
	.BackgroundImage > img{
		height: 100;
		opacity: 16%;
	}
	.imageA{
		margin-left:50%;
		display: inline-block;
		scale: 150%;
		margin-top: 9%;
	}
	.imageB{
		margin-left:10%;
	}
	.imageC{
		margin-left: 30%;
	}
</style>