'use client';

import { useState } from 'react';
import axios from 'axios';
import { Brain, Activity, TrendingUp, AlertCircle, CheckCircle2, Clock } from 'lucide-react';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export default function Home() {
  const [userId, setUserId] = useState('');
  const [recommendations, setRecommendations] = useState(null);
  const [activities, setActivities] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [activeTab, setActiveTab] = useState('recommend');

  const fetchRecommendations = async () => {
    if (!userId.trim()) {
      setError('Please enter a user ID');
      return;
    }

    setLoading(true);
    setError('');
    
    try {
      const response = await axios.post(`${API_URL}/api/recommend`, {
        user_id: userId,
        limit: 10
      });
      
      setRecommendations(response.data);
      setError('');
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to fetch recommendations');
      setRecommendations(null);
    } finally {
      setLoading(false);
    }
  };

  const fetchActivities = async () => {
    if (!userId.trim()) {
      setError('Please enter a user ID');
      return;
    }

    setLoading(true);
    setError('');
    
    try {
      const response = await axios.get(`${API_URL}/api/activity/${userId}?limit=20`);
      setActivities(response.data);
      setError('');
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to fetch activities');
      setActivities(null);
    } finally {
      setLoading(false);
    }
  };

  const getPriorityColor = (priority) => {
    switch(priority.toLowerCase()) {
      case 'high': return 'text-red-600 bg-red-50 border-red-200';
      case 'medium': return 'text-yellow-600 bg-yellow-50 border-yellow-200';
      case 'low': return 'text-green-600 bg-green-50 border-green-200';
      default: return 'text-gray-600 bg-gray-50 border-gray-200';
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b">
        <div className="max-w-6xl mx-auto px-6 py-4">
          <div className="flex items-center gap-3">
            <Brain className="w-8 h-8 text-blue-600" />
            <div>
              <h1 className="text-2xl font-bold text-gray-900">
                AI Recommendation Agent
              </h1>
              <p className="text-sm text-gray-600">
                Intelligent insights from your activity patterns
              </p>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-6xl mx-auto px-6 py-8">
        {/* Input Section */}
        <div className="bg-white rounded-xl shadow-md p-6 mb-8">
          <label className="block text-sm font-medium text-gray-700 mb-2">
            User ID
          </label>
          <div className="flex gap-3">
            <input
              type="text"
              value={userId}
              onChange={(e) => setUserId(e.target.value)}
              placeholder="e.g., sales_rep_001, customer_success_001"
              className="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              onKeyPress={(e) => e.key === 'Enter' && (activeTab === 'recommend' ? fetchRecommendations() : fetchActivities())}
            />
            <button
              onClick={activeTab === 'recommend' ? fetchRecommendations : fetchActivities}
              disabled={loading}
              className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors flex items-center gap-2"
            >
              {loading ? (
                <>
                  <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin" />
                  Loading...
                </>
              ) : activeTab === 'recommend' ? (
                <>
                  <TrendingUp className="w-4 h-4" />
                  Get Recommendations
                </>
              ) : (
                <>
                  <Activity className="w-4 h-4" />
                  View Activities
                </>
              )}
            </button>
          </div>

          {/* Sample Users */}
          <div className="mt-4 p-4 bg-blue-50 rounded-lg">
            <p className="text-sm font-medium text-blue-900 mb-2">💡 Try these sample users:</p>
            <div className="flex flex-wrap gap-2">
              {['sales_rep_001', 'customer_success_001', 'product_manager_001'].map(user => (
                <button
                  key={user}
                  onClick={() => setUserId(user)}
                  className="px-3 py-1 bg-white text-blue-700 text-sm rounded-md hover:bg-blue-100 transition-colors"
                >
                  {user}
                </button>
              ))}
            </div>
          </div>
        </div>

        {/* Tabs */}
        <div className="flex gap-4 mb-6">
          <button
            onClick={() => setActiveTab('recommend')}
            className={`px-6 py-2 rounded-lg font-medium transition-colors ${
              activeTab === 'recommend'
                ? 'bg-blue-600 text-white'
                : 'bg-white text-gray-600 hover:bg-gray-50'
            }`}
          >
            <TrendingUp className="w-4 h-4 inline mr-2" />
            Recommendations
          </button>
          <button
            onClick={() => setActiveTab('activities')}
            className={`px-6 py-2 rounded-lg font-medium transition-colors ${
              activeTab === 'activities'
                ? 'bg-blue-600 text-white'
                : 'bg-white text-gray-600 hover:bg-gray-50'
            }`}
          >
            <Activity className="w-4 h-4 inline mr-2" />
            Activity Log
          </button>
        </div>

        {/* Error Message */}
        {error && (
          <div className="bg-red-50 border border-red-200 rounded-lg p-4 mb-6 flex items-start gap-3">
            <AlertCircle className="w-5 h-5 text-red-600 flex-shrink-0 mt-0.5" />
            <div className="text-red-800">{error}</div>
          </div>
        )}

        {/* Recommendations Display */}
        {activeTab === 'recommend' && recommendations && (
          <div className="space-y-4">
            <div className="bg-white rounded-xl shadow-md p-6">
              <div className="flex items-center justify-between mb-6">
                <h2 className="text-xl font-bold text-gray-900 flex items-center gap-2">
                  <Brain className="w-6 h-6 text-blue-600" />
                  AI-Generated Recommendations
                </h2>
                <span className="text-sm text-gray-500">
                  for {recommendations.user_id}
                </span>
              </div>

              <div className="space-y-4">
                {recommendations.recommendations.map((rec, index) => (
                  <div
                    key={index}
                    className="border rounded-lg p-5 hover:shadow-md transition-shadow"
                  >
                    <div className="flex items-start justify-between mb-3">
                      <div className="flex items-center gap-3">
                        <span className="flex items-center justify-center w-8 h-8 rounded-full bg-blue-100 text-blue-700 font-bold text-sm">
                          {index + 1}
                        </span>
                        <h3 className="font-semibold text-gray-900">{rec.action}</h3>
                      </div>
                      <span className={`px-3 py-1 rounded-full text-xs font-medium border ${getPriorityColor(rec.priority)}`}>
                        {rec.priority}
                      </span>
                    </div>
                    <p className="text-gray-600 text-sm ml-11">{rec.reason}</p>
                  </div>
                ))}
              </div>

              <div className="mt-6 pt-6 border-t text-sm text-gray-500 flex items-center gap-2">
                <Clock className="w-4 h-4" />
                Analysis completed at {new Date(recommendations.analysis_timestamp).toLocaleString()}
              </div>
            </div>
          </div>
        )}

        {/* Activities Display */}
        {activeTab === 'activities' && activities && (
          <div className="bg-white rounded-xl shadow-md p-6">
            <div className="flex items-center justify-between mb-6">
              <h2 className="text-xl font-bold text-gray-900 flex items-center gap-2">
                <Activity className="w-6 h-6 text-purple-600" />
                Recent Activity Log
              </h2>
              <span className="text-sm text-gray-500">
                {activities.count} activities found
              </span>
            </div>

            <div className="space-y-3">
              {activities.activities.map((activity) => (
                <div
                  key={activity.id}
                  className="flex items-start gap-4 p-4 border rounded-lg hover:bg-gray-50 transition-colors"
                >
                  <div className="flex-shrink-0 w-2 h-2 mt-2 bg-purple-500 rounded-full" />
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-3 mb-1">
                      <span className="font-medium text-gray-900">{activity.action}</span>
                      <span className="text-xs text-gray-500">
                        {new Date(activity.timestamp).toLocaleString()}
                      </span>
                    </div>
                    {activity.context && (
                      <p className="text-sm text-gray-600">{activity.context}</p>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Empty State */}
        {!recommendations && !activities && !error && !loading && (
          <div className="bg-white rounded-xl shadow-md p-12 text-center">
            <Brain className="w-16 h-16 text-gray-300 mx-auto mb-4" />
            <h3 className="text-xl font-semibold text-gray-700 mb-2">
              Ready to analyze
            </h3>
            <p className="text-gray-500">
              Enter a user ID above and click the button to get started
            </p>
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="mt-16 py-6 border-t bg-white">
        <div className="max-w-6xl mx-auto px-6 text-center text-sm text-gray-600">
          <p>AI-Powered Recommendation System • Built with FastAPI, Next.js & AI</p>
        </div>
      </footer>
    </div>
  );
}
