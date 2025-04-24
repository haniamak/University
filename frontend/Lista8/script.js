const pokemonListElement = document.getElementById("pokemonList");
const errorText = document.getElementById("errorText");
const pokemonDetailsElement = document.getElementById("pokemonDetails");
const pokemonNameElement = document.getElementById("pokemonName");
const pokemonImageElement = document.getElementById("pokemonImg");
const pokemonTypeElement = document.getElementById("pokemonTypes");
const pokemonStatsElement = document.getElementById("pokemonStats");
const pokemonFlavorTextElement = document.getElementById("pokemonFlavorText");
const loading = document.getElementById("loading");


pokemonListElement.innerHTML = "";
pokemonDetailsElement.style.display = "none";


function capitalize(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

async function preloadImage(src) {
  const img = new Image();
  img.src = src;
  await img.decode();
  return img;
}

async function fetchPokemonList() {
  loading.style.display = "block";
  pokemonListElement.innerHTML = "";
  try {
    const res = await fetch("https://pokeapi.co/api/v2/pokemon-species?limit=151");
    const data = await res.json();

    data.results.forEach((pokemon) => {
      const li = document.createElement("li");
      li.textContent = capitalize(pokemon.name);
      li.addEventListener("click", () => loadPokemon(pokemon.name));
      pokemonListElement.appendChild(li);
    });
  } catch (err) {
    console.error("Error loading Pokémon list:", err);
    errorText.style.display = "block";
  } finally {
    loading.style.display = "none";
  }
} 

async function loadPokemon(pokemonName) {
  loading.style.display = "block";
  pokemonDetailsElement.style.display = "none";
  try {
    const url = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonName}`);
    const pokemonData = await url.json();

    pokemonNameElement.textContent = capitalize(pokemonData.name);
    console.log(pokemonData);

    const spriteUrl = pokemonData.sprites.front_default;
    const preloadedImg = await preloadImage(spriteUrl);
    pokemonImageElement.src = pokemonData.sprites.front_default;
    pokemonImageElement.alt = pokemonData.name;
    pokemonImageElement.style.display = "block";

    pokemonTypeElement.innerHTML = "";
    pokemonData.types.forEach(type => {
      const typeSpan = document.createElement("span");
      typeSpan.className = "type";
      typeSpan.textContent = capitalize(type.type.name);
      pokemonTypeElement.appendChild(typeSpan);
    });

    pokemonStatsElement.innerHTML = "";
    pokemonData.stats.forEach(stat => {
      const statDiv = document.createElement("div");
      statDiv.className = "stat";

      const statName = document.createElement("span");
      statName.textContent = capitalize(stat.stat.name);

      const statValue = document.createElement("span");
      statValue.textContent = stat.base_stat;

      statDiv.appendChild(statName);
      statDiv.appendChild(statValue);
      pokemonStatsElement.appendChild(statDiv);
    });

    const flavorTextRes = await fetch(`https://pokeapi.co/api/v2/pokemon-species/${pokemonName}`);
    const flavorTextData = await flavorTextRes.json();
    const flavorText = flavorTextData.flavor_text_entries.find(entry => entry.language.name === "en");
    pokemonFlavorTextElement.textContent = flavorText ? flavorText.flavor_text.replace(/[\n\f]/g, " ") : "No flavor text available.";
    pokemonFlavorTextElement.style.display = "block";
    pokemonDetailsElement.style.display = "flex";

  }
  catch (err) {
    console.error("Error loading Pokémon details:", err);
    errorText.style.display = "block";
  }
  finally {
    loading.style.display = "none";
  }
}

fetchPokemonList();