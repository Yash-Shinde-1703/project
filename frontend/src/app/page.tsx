'use client';

import { useState } from 'react';

export default function Home() {
  const [movieInput, setMovieInput] = useState('');
  const [recommendations, setRecommendations] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const getRecommendations = async () => {
    if (!movieInput.trim()) return;

    setLoading(true);
    setError('');
    setRecommendations([]);

    try {
      const response = await fetch('http://localhost:8000/recommend', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          movie_title: movieInput.trim(),
          top_n: 6,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || 'Failed to fetch recommendations');
      }

      setRecommendations(data.recommendations);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen px-4 py-16 md:py-24">
      <div className="max-w-4xl mx-auto">
        <header className="text-center mb-16">
          <h1 className="text-6xl md:text-7xl font-extrabold tracking-tight mb-6">
            Cine<span className="text-indigo-500">Match</span>
          </h1>
          <p className="text-xl text-slate-400">
            Discover your next cinematic adventure with AI-powered recommendations.
          </p>
        </header>

        <section className="mb-16">
          <div className="glass p-2 rounded-[24px] flex flex-col md:flex-row gap-2 shadow-indigo-500/10">
            <input
              type="text"
              value={movieInput}
              onChange={(e) => setMovieInput(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && getRecommendations()}
              placeholder="Enter a movie you love (e.g., Inception)..."
              className="flex-1 bg-transparent border-none outline-none px-6 py-4 text-lg text-white placeholder:text-slate-500"
            />
            <button
              onClick={getRecommendations}
              className="bg-indigo-600 hover:bg-indigo-500 text-white font-semibold px-8 py-4 rounded-[18px] transition-all active:scale-95 shadow-lg shadow-indigo-600/20"
            >
              Find Matches
            </button>
          </div>
        </section>

        {loading && (
          <div className="text-center py-12">
            <div className="inline-block w-12 h-12 border-4 border-slate-700 border-t-indigo-500 rounded-full animate-spin mb-4" />
            <p className="text-slate-400 font-medium animate-pulse">Analyzing cinematic patterns...</p>
          </div>
        )}

        {error && (
          <div className="bg-red-500/10 border border-red-500/20 text-red-400 p-4 rounded-xl text-center mb-8">
            {error}
          </div>
        )}

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {recommendations.map((movie, index) => (
            <div
              key={movie}
              className="glass glass-hover p-8 rounded-[32px] animate-in fade-in slide-in-from-bottom-4 duration-500 fill-mode-both"
              style={{ animationDelay: `${index * 100}ms` }}
            >
              <span className="inline-block px-3 py-1 bg-indigo-500/10 text-indigo-400 text-xs font-bold rounded-full mb-4">
                RECOMMENDATION #{index + 1}
              </span>
              <h3 className="text-2xl font-bold mb-2">{movie}</h3>
              <p className="text-slate-400 text-sm leading-relaxed">
                Matched based on your interest in <span className="text-indigo-300 font-medium">{movieInput}</span>.
              </p>
            </div>
          ))}
        </div>
      </div>
    </main>
  );
}
