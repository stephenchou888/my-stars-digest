import React, { useEffect, useMemo, useState } from "react"
import {
  Activity,
  AlertTriangle,
  Archive,
  BookmarkCheck,
  Check,
  Copy,
  ExternalLink,
  FileText,
  Filter,
  GitFork,
  Github,
  KeyRound,
  LayoutGrid,
  List,
  Moon,
  RefreshCw,
  Rocket,
  Search,
  Sparkles,
  Star,
  Sun,
  Trash2,
} from "lucide-react"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Input } from "@/components/ui/input"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog"

interface ReleaseInfo {
  tag: string
  url: string
  published_at: string
  summary_zh: string
  raw_body: string
}

interface RepoItem {
  id: number
  repo: string
  name: string
  owner: string
  avatar_url: string
  html_url: string
  description: string
  desc_zh: string
  stars: number
  forks: number
  open_issues: number
  language: string
  topics: string[]
  category: string
  status: "active" | "stale" | "abandoned"
  reason: string
  days_since_push: number
  pushed_at: string
  created_at: string
  archived: boolean
  homepage: string
  release: ReleaseInfo | null
}

interface DashboardData {
  generated_at: string
  date: string
  username: string
  stats: {
    total: number
    active_releases: number
    active_health: number
    stale_health: number
    abandoned: number
    categories: Record<string, number>
    languages: Record<string, number>
  }
  repos: RepoItem[]
}

const STORAGE_TOKEN_KEY = "stars_radar_gh_token"
const STORAGE_KEEP_KEY = "stars_radar_keep_repos"
const STORAGE_UNSTARRED_KEY = "stars_radar_unstarred_repos"

export default function App() {
  const [data, setData] = useState<DashboardData | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [darkMode, setDarkMode] = useState(true)

  // Filters & view state
  const [activeTab, setActiveTab] = useState<string>("releases")
  const [search, setSearch] = useState("")
  const [selectedCategory, setSelectedCategory] = useState<string>("ALL")
  const [selectedLanguage, setSelectedLanguage] = useState<string>("ALL")
  const [selectedStatus, setSelectedStatus] = useState<string>("ALL")
  const [sortBy, setSortBy] = useState<string>("release")
  const [viewMode, setViewMode] = useState<"grid" | "table">("grid")

  // Management state
  const [selectedRepos, setSelectedRepos] = useState<Set<string>>(new Set())
  const [keepRepos, setKeepRepos] = useState<Set<string>>(() => {
    try {
      const saved = localStorage.getItem(STORAGE_KEEP_KEY)
      return saved ? new Set(JSON.parse(saved)) : new Set()
    } catch {
      return new Set()
    }
  })
  const [unstarredRepos, setUnstarredRepos] = useState<Set<string>>(() => {
    try {
      const saved = localStorage.getItem(STORAGE_UNSTARRED_KEY)
      return saved ? new Set(JSON.parse(saved)) : new Set()
    } catch {
      return new Set()
    }
  })
  const [ghToken, setGhToken] = useState<string>(() => localStorage.getItem(STORAGE_TOKEN_KEY) || "")
  const [tokenInput, setTokenInput] = useState<string>(() => localStorage.getItem(STORAGE_TOKEN_KEY) || "")
  const [tokenModalOpen, setTokenModalOpen] = useState(false)
  const [detailRepo, setDetailRepo] = useState<RepoItem | null>(null)
  const [unstarBusy, setUnstarBusy] = useState<string | null>(null)
  const [copiedCmd, setCopiedCmd] = useState(false)
  const [toastMsg, setToastMsg] = useState<string | null>(null)

  useEffect(() => {
    const root = document.documentElement
    if (darkMode) {
      root.classList.add("dark")
    } else {
      root.classList.remove("dark")
    }
  }, [darkMode])

  const showToast = (msg: string) => {
    setToastMsg(msg)
    setTimeout(() => setToastMsg(null), 3200)
  }

  const fetchData = async () => {
    setLoading(true)
    setError(null)
    try {
      const resp = await fetch(`./data/dashboard.json?t=${Date.now()}`)
      if (!resp.ok) throw new Error(`HTTP ${resp.status}`)
      const json: DashboardData = await resp.json()
      setData(json)
    } catch (e: any) {
      setError(e?.message || "加载看板数据失败")
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchData()
  }, [])

  const saveToken = () => {
    const trimmed = tokenInput.trim()
    setGhToken(trimmed)
    if (trimmed) {
      localStorage.setItem(STORAGE_TOKEN_KEY, trimmed)
      showToast("✅ 已保存 GitHub Token（仅保存在您的浏览器本地）")
    } else {
      localStorage.removeItem(STORAGE_TOKEN_KEY)
      showToast("已清除本地 GitHub Token")
    }
    setTokenModalOpen(false)
  }

  const toggleKeepRepo = (fullName: string) => {
    const next = new Set(keepRepos)
    if (next.has(fullName)) {
      next.delete(fullName)
      showToast(`已从保留白名单移除 ${fullName}`)
    } else {
      next.add(fullName)
      showToast(`🛡️ 已将 ${fullName} 加入保留白名单`)
    }
    setKeepRepos(next)
    localStorage.setItem(STORAGE_KEEP_KEY, JSON.stringify(Array.from(next)))
  }

  const toggleSelectRepo = (fullName: string) => {
    const next = new Set(selectedRepos)
    if (next.has(fullName)) {
      next.delete(fullName)
    } else {
      next.add(fullName)
    }
    setSelectedRepos(next)
  }

  const handleUnstarSingle = async (fullName: string, htmlUrl: string) => {
    if (!ghToken) {
      window.open(htmlUrl, "_blank", "noopener,noreferrer")
      return
    }
    setUnstarBusy(fullName)
    try {
      const resp = await fetch(`https://api.github.com/user/starred/${fullName}`, {
        method: "DELETE",
        headers: {
          Authorization: `Bearer ${ghToken}`,
          Accept: "application/vnd.github.v3+json",
        },
      })
      if (resp.status === 204 || resp.status === 404) {
        const next = new Set(unstarredRepos)
        next.add(fullName)
        setUnstarredRepos(next)
        localStorage.setItem(STORAGE_UNSTARRED_KEY, JSON.stringify(Array.from(next)))
        const nextSel = new Set(selectedRepos)
        nextSel.delete(fullName)
        setSelectedRepos(nextSel)
        showToast(`✅ 已成功取消 Star: ${fullName}`)
      } else {
        showToast(`❌ 取消 Star 失败 (HTTP ${resp.status})，请检查 Token 是否勾选 public_repo 权限`)
      }
    } catch (e: any) {
      showToast(`❌ 网络异常: ${e?.message}`)
    } finally {
      setUnstarBusy(null)
    }
  }

  const handleBatchUnstar = async () => {
    if (selectedRepos.size === 0) return
    if (!ghToken) {
      setTokenModalOpen(true)
      return
    }
    const targets = Array.from(selectedRepos)
    setUnstarBusy("BATCH")
    let successCount = 0
    const nextUnstarred = new Set(unstarredRepos)

    for (const fullName of targets) {
      try {
        const resp = await fetch(`https://api.github.com/user/starred/${fullName}`, {
          method: "DELETE",
          headers: {
            Authorization: `Bearer ${ghToken}`,
            Accept: "application/vnd.github.v3+json",
          },
        })
        if (resp.status === 204 || resp.status === 404) {
          successCount++
          nextUnstarred.add(fullName)
        }
      } catch {
        // ignore individual failure
      }
    }
    setUnstarredRepos(nextUnstarred)
    localStorage.setItem(STORAGE_UNSTARRED_KEY, JSON.stringify(Array.from(nextUnstarred)))
    setSelectedRepos(new Set())
    setUnstarBusy(null)
    showToast(`🎉 批量处理完成：成功取消 ${successCount} / ${targets.length} 个仓库的 Star`)
  }

  const copyGhCliCommands = () => {
    const targets = Array.from(selectedRepos)
    if (targets.length === 0) return
    const cmd = targets.map((r) => `gh api -X DELETE /user/starred/${r}`).join("\n")
    navigator.clipboard.writeText(cmd)
    setCopiedCmd(true)
    showToast(`📋 已复制 ${targets.length} 条 gh CLI 取消 Star 命令`)
    setTimeout(() => setCopiedCmd(false), 2000)
  }

  const visibleRepos = useMemo(() => {
    if (!data) return []
    return data.repos.filter((r) => !unstarredRepos.has(r.repo))
  }, [data, unstarredRepos])

  const categoriesList = useMemo(() => {
    const counts: Record<string, number> = {}
    for (const r of visibleRepos) {
      counts[r.category] = (counts[r.category] || 0) + 1
    }
    return Object.entries(counts).sort((a, b) => b[1] - a[1])
  }, [visibleRepos])

  const languagesList = useMemo(() => {
    const counts: Record<string, number> = {}
    for (const r of visibleRepos) {
      const lang = r.language || "Other"
      counts[lang] = (counts[lang] || 0) + 1
    }
    return Object.entries(counts).sort((a, b) => b[1] - a[1])
  }, [visibleRepos])

  const filteredRepos = useMemo(() => {
    let list = visibleRepos

    // Tab filter
    if (activeTab === "releases") {
      list = list.filter((r) => r.release !== null)
    } else if (activeTab === "cleanup") {
      list = list.filter((r) => r.status === "abandoned" || r.status === "stale")
    }

    // Status filter
    if (selectedStatus !== "ALL") {
      if (selectedStatus === "RELEASE") {
        list = list.filter((r) => r.release !== null)
      } else if (selectedStatus === "KEEP") {
        list = list.filter((r) => keepRepos.has(r.repo))
      } else {
        list = list.filter((r) => r.status === selectedStatus)
      }
    }

    // Category filter
    if (selectedCategory !== "ALL") {
      list = list.filter((r) => r.category === selectedCategory)
    }

    // Language filter
    if (selectedLanguage !== "ALL") {
      list = list.filter((r) => (r.language || "Other") === selectedLanguage)
    }

    // Search query
    if (search.trim()) {
      const q = search.toLowerCase().trim()
      list = list.filter(
        (r) =>
          r.repo.toLowerCase().includes(q) ||
          (r.desc_zh && r.desc_zh.toLowerCase().includes(q)) ||
          (r.description && r.description.toLowerCase().includes(q)) ||
          r.topics.some((t) => t.toLowerCase().includes(q)) ||
          (r.release?.summary_zh && r.release.summary_zh.toLowerCase().includes(q))
      )
    }

    // Sort
    const sorted = [...list]
    sorted.sort((a, b) => {
      if (sortBy === "release") {
        const da = a.release?.published_at || ""
        const db = b.release?.published_at || ""
        if (da !== db) return db.localeCompare(da)
        return b.stars - a.stars
      }
      if (sortBy === "stars") return b.stars - a.stars
      if (sortBy === "recent_push") return a.days_since_push - b.days_since_push
      if (sortBy === "oldest_push") return b.days_since_push - a.days_since_push
      if (sortBy === "name") return a.repo.localeCompare(b.repo)
      return 0
    })

    return sorted
  }, [
    visibleRepos,
    activeTab,
    selectedStatus,
    selectedCategory,
    selectedLanguage,
    search,
    sortBy,
    keepRepos,
  ])

  const statsSummary = useMemo(() => {
    const total = visibleRepos.length
    const releases = visibleRepos.filter((r) => r.release !== null).length
    const active = visibleRepos.filter((r) => r.status === "active").length
    const stale = visibleRepos.filter((r) => r.status === "stale").length
    const abandoned = visibleRepos.filter((r) => r.status === "abandoned").length
    return { total, releases, active, stale, abandoned }
  }, [visibleRepos])

  const renderStatusBadge = (repo: RepoItem) => {
    if (keepRepos.has(repo.repo)) {
      return <Badge variant="secondary">🛡️ 白名单保留</Badge>
    }
    if (repo.archived) {
      return <Badge variant="danger">🗄️ 已归档 (Archived)</Badge>
    }
    if (repo.status === "active") {
      return <Badge variant="success">💚 {repo.reason}</Badge>
    }
    if (repo.status === "stale") {
      return <Badge variant="warning">🟡 {repo.reason}</Badge>
    }
    return <Badge variant="danger">🛑 {repo.reason}</Badge>
  }

  if (loading) {
    return (
      <div className="flex min-h-screen flex-col items-center justify-center gap-3">
        <RefreshCw className="h-8 w-8 animate-spin text-primary" />
        <p className="text-sm text-muted-foreground">正在加载 Starred 项目雷达看板数据...</p>
      </div>
    )
  }

  if (error || !data) {
    return (
      <div className="flex min-h-screen flex-col items-center justify-center gap-4 p-6 text-center">
        <AlertTriangle className="h-10 w-10 text-destructive" />
        <h2 className="text-lg font-semibold">无法加载看板数据</h2>
        <p className="text-sm text-muted-foreground">{error}</p>
        <Button onClick={fetchData}>重试加载</Button>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-background pb-20">
      {/* Top Toast */}
      {toastMsg && (
        <div className="fixed bottom-6 right-6 z-50 flex items-center gap-2 rounded-lg border bg-card px-4 py-3 text-sm font-medium shadow-xl">
          <span>{toastMsg}</span>
        </div>
      )}

      {/* Header */}
      <header className="sticky top-0 z-30 border-b bg-background/85 backdrop-blur-md">
        <div className="mx-auto flex max-w-7xl flex-wrap items-center justify-between gap-4 px-4 py-3.5 sm:px-6">
          <div className="flex items-center gap-3">
            <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-primary text-primary-foreground shadow">
              <Sparkles className="h-5 w-5" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h1 className="text-lg font-bold tracking-tight sm:text-xl">
                  Starred 项目雷达看板
                </h1>
                <Badge variant="outline" className="hidden sm:inline-flex">
                  shadcn/ui
                </Badge>
              </div>
              <p className="text-xs text-muted-foreground">
                @{data.username} · 数据更新于 {data.generated_at}
              </p>
            </div>
          </div>

          <div className="flex items-center gap-2">
            <Button
              variant={ghToken ? "secondary" : "outline"}
              size="sm"
              onClick={() => setTokenModalOpen(true)}
            >
              <KeyRound className="h-4 w-4" />
              <span>{ghToken ? "已连接 Token (可直连取消Star)" : "连接 Token 管理"}</span>
            </Button>

            <Button
              variant="outline"
              size="sm"
              asChild
            >
              <a
                href={`https://github.com/${data.username}/my-stars-digest/actions`}
                target="_blank"
                rel="noopener noreferrer"
              >
                <RefreshCw className="h-3.5 w-3.5" />
                <span className="hidden md:inline">Actions 同步</span>
              </a>
            </Button>

            <Button
              variant="outline"
              size="icon"
              asChild
              title="前往 GitHub 仓库"
            >
              <a
                href={`https://github.com/${data.username}/my-stars-digest`}
                target="_blank"
                rel="noopener noreferrer"
              >
                <Github className="h-4 w-4" />
              </a>
            </Button>

            <Button
              variant="ghost"
              size="icon"
              onClick={() => setDarkMode(!darkMode)}
              title="切换深色/浅色主题"
            >
              {darkMode ? <Sun className="h-4 w-4" /> : <Moon className="h-4 w-4" />}
            </Button>
          </div>
        </div>
      </header>

      <main className="mx-auto max-w-7xl space-y-6 px-4 pt-6 sm:px-6">
        {/* KPI Stat Cards */}
        <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-5">
          <Card
            onClick={() => {
              setActiveTab("all")
              setSelectedStatus("ALL")
            }}
            className={`cursor-pointer transition-all hover:border-primary/50 ${
              activeTab === "all" && selectedStatus === "ALL" ? "ring-2 ring-primary" : ""
            }`}
          >
            <CardHeader className="p-4 pb-2">
              <CardDescription className="flex items-center justify-between text-xs">
                <span>🌟 总关注项目</span>
                <Star className="h-4 w-4 text-amber-400" />
              </CardDescription>
              <CardTitle className="text-2xl font-bold">{statsSummary.total}</CardTitle>
            </CardHeader>
            <CardContent className="p-4 pt-0 text-xs text-muted-foreground">
              涵盖 {categoriesList.length} 个技术领域
            </CardContent>
          </Card>

          <Card
            onClick={() => {
              setActiveTab("releases")
              setSelectedStatus("ALL")
              setSortBy("release")
            }}
            className={`cursor-pointer transition-all hover:border-primary/50 ${
              activeTab === "releases" ? "ring-2 ring-primary" : ""
            }`}
          >
            <CardHeader className="p-4 pb-2">
              <CardDescription className="flex items-center justify-between text-xs">
                <span>🚀 近30天新发版</span>
                <Rocket className="h-4 w-4 text-blue-400" />
              </CardDescription>
              <CardTitle className="text-2xl font-bold text-blue-500 dark:text-blue-400">
                {statsSummary.releases}
              </CardTitle>
            </CardHeader>
            <CardContent className="p-4 pt-0 text-xs text-muted-foreground">
              含自动提炼中文更新亮点
            </CardContent>
          </Card>

          <Card
            onClick={() => {
              setActiveTab("all")
              setSelectedStatus("active")
              setSortBy("recent_push")
            }}
            className={`cursor-pointer transition-all hover:border-primary/50 ${
              selectedStatus === "active" ? "ring-2 ring-primary" : ""
            }`}
          >
            <CardHeader className="p-4 pb-2">
              <CardDescription className="flex items-center justify-between text-xs">
                <span>💚 活跃维护 (&lt;90天)</span>
                <Activity className="h-4 w-4 text-emerald-400" />
              </CardDescription>
              <CardTitle className="text-2xl font-bold text-emerald-600 dark:text-emerald-400">
                {statsSummary.active}
              </CardTitle>
            </CardHeader>
            <CardContent className="p-4 pt-0 text-xs text-muted-foreground">
              近期有持续代码提交
            </CardContent>
          </Card>

          <Card
            onClick={() => {
              setActiveTab("cleanup")
              setSelectedStatus("stale")
              setSortBy("oldest_push")
            }}
            className={`cursor-pointer transition-all hover:border-primary/50 ${
              selectedStatus === "stale" ? "ring-2 ring-primary" : ""
            }`}
          >
            <CardHeader className="p-4 pb-2">
              <CardDescription className="flex items-center justify-between text-xs">
                <span>🟡 低频维护 (90-365天)</span>
                <AlertTriangle className="h-4 w-4 text-amber-400" />
              </CardDescription>
              <CardTitle className="text-2xl font-bold text-amber-600 dark:text-amber-400">
                {statsSummary.stale}
              </CardTitle>
            </CardHeader>
            <CardContent className="p-4 pt-0 text-xs text-muted-foreground">
              超 3 个月未提交代码
            </CardContent>
          </Card>

          <Card
            onClick={() => {
              setActiveTab("cleanup")
              setSelectedStatus("abandoned")
              setSortBy("oldest_push")
            }}
            className={`col-span-2 sm:col-span-1 cursor-pointer transition-all hover:border-destructive/60 ${
              activeTab === "cleanup" && selectedStatus === "abandoned"
                ? "ring-2 ring-destructive"
                : ""
            }`}
          >
            <CardHeader className="p-4 pb-2">
              <CardDescription className="flex items-center justify-between text-xs">
                <span>🛑 建议清理 (&gt;1年/归档)</span>
                <Archive className="h-4 w-4 text-rose-400" />
              </CardDescription>
              <CardTitle className="text-2xl font-bold text-rose-600 dark:text-rose-400">
                {statsSummary.abandoned}
              </CardTitle>
            </CardHeader>
            <CardContent className="p-4 pt-0 text-xs text-muted-foreground">
              点击进入批量清理工作台
            </CardContent>
          </Card>
        </div>

        {/* Category Pills */}
        <div className="flex flex-wrap items-center gap-2">
          <Button
            variant={selectedCategory === "ALL" ? "default" : "outline"}
            size="sm"
            onClick={() => setSelectedCategory("ALL")}
            className="h-8 rounded-full text-xs"
          >
            全部领域 ({visibleRepos.length})
          </Button>
          {categoriesList.map(([cat, count]) => (
            <Button
              key={cat}
              variant={selectedCategory === cat ? "default" : "outline"}
              size="sm"
              onClick={() => setSelectedCategory(selectedCategory === cat ? "ALL" : cat)}
              className="h-8 rounded-full text-xs"
            >
              {cat} ({count})
            </Button>
          ))}
        </div>

        {/* Tabs & Filter Controls */}
        <Tabs
          value={activeTab}
          onValueChange={(val) => {
            setActiveTab(val)
            if (val === "releases") {
              setSelectedStatus("ALL")
              setSortBy("release")
            } else if (val === "cleanup") {
              setSelectedStatus("abandoned")
              setSortBy("oldest_push")
            } else {
              setSelectedStatus("ALL")
              setSortBy("stars")
            }
          }}
        >
          <div className="flex flex-col gap-3 lg:flex-row lg:items-center lg:justify-between">
            <TabsList className="w-full sm:w-auto">
              <TabsTrigger value="releases" className="flex-1 sm:flex-initial">
                🚀 本期更新 ({statsSummary.releases})
              </TabsTrigger>
              <TabsTrigger value="all" className="flex-1 sm:flex-initial">
                📚 全部关注库 ({statsSummary.total})
              </TabsTrigger>
              <TabsTrigger value="cleanup" className="flex-1 sm:flex-initial">
                🛑 弃坑清理台 ({statsSummary.abandoned + statsSummary.stale})
              </TabsTrigger>
            </TabsList>

            {/* Search & Filters */}
            <div className="flex flex-wrap items-center gap-2">
              <div className="relative min-w-[220px] flex-1 sm:w-64">
                <Search className="absolute left-2.5 top-2.5 h-4 w-4 text-muted-foreground" />
                <Input
                  placeholder="搜索仓库名、中文简介、标签、更新内容..."
                  value={search}
                  onChange={(e) => setSearch(e.target.value)}
                  className="pl-8"
                />
              </div>

              <select
                value={selectedLanguage}
                onChange={(e) => setSelectedLanguage(e.target.value)}
                className="h-9 rounded-md border border-input bg-background px-3 text-xs shadow-sm focus:outline-none focus:ring-1 focus:ring-ring"
              >
                <option value="ALL">💻 全部语言</option>
                {languagesList.map(([lang, count]) => (
                  <option key={lang} value={lang}>
                    {lang} ({count})
                  </option>
                ))}
              </select>

              <select
                value={selectedStatus}
                onChange={(e) => setSelectedStatus(e.target.value)}
                className="h-9 rounded-md border border-input bg-background px-3 text-xs shadow-sm focus:outline-none focus:ring-1 focus:ring-ring"
              >
                <option value="ALL">⚡ 全部状态</option>
                <option value="active">💚 活跃维护 (&lt;90天)</option>
                <option value="stale">🟡 低频维护 (90-365天)</option>
                <option value="abandoned">🛑 停更/归档 (&gt;1年)</option>
                <option value="RELEASE">🚀 近期有新 Release</option>
                <option value="KEEP">🛡️ 白名单保留 ({keepRepos.size})</option>
              </select>

              <select
                value={sortBy}
                onChange={(e) => setSortBy(e.target.value)}
                className="h-9 rounded-md border border-input bg-background px-3 text-xs shadow-sm focus:outline-none focus:ring-1 focus:ring-ring"
              >
                <option value="release">📅 按最新发布排序</option>
                <option value="stars">⭐ 按 Star 数从高到低</option>
                <option value="recent_push">🔥 按最近代码提交排序</option>
                <option value="oldest_push">⏳ 按停更天数从高到低</option>
                <option value="name">🔤 按仓库名 A-Z</option>
              </select>

              <div className="flex items-center rounded-md border p-0.5">
                <Button
                  variant={viewMode === "grid" ? "secondary" : "ghost"}
                  size="icon"
                  className="h-7 w-7"
                  onClick={() => setViewMode("grid")}
                  title="卡片视图"
                >
                  <LayoutGrid className="h-3.5 w-3.5" />
                </Button>
                <Button
                  variant={viewMode === "table" ? "secondary" : "ghost"}
                  size="icon"
                  className="h-7 w-7"
                  onClick={() => setViewMode("table")}
                  title="表格管理视图"
                >
                  <List className="h-3.5 w-3.5" />
                </Button>
              </div>
            </div>
          </div>

          {/* Batch Management Bar */}
          {(activeTab === "cleanup" || selectedRepos.size > 0) && (
            <div className="mt-3 flex flex-wrap items-center justify-between gap-3 rounded-xl border bg-muted/40 p-3">
              <div className="flex flex-wrap items-center gap-2 text-xs">
                <Filter className="h-4 w-4 text-muted-foreground" />
                <span>
                  当前筛选共 <strong>{filteredRepos.length}</strong> 个项目，已勾选{" "}
                  <strong className="text-primary">{selectedRepos.size}</strong> 个
                </span>
                <Button
                  variant="outline"
                  size="sm"
                  className="h-7 text-xs"
                  onClick={() => {
                    const next = new Set(selectedRepos)
                    filteredRepos.forEach((r) => {
                      if (!keepRepos.has(r.repo)) next.add(r.repo)
                    })
                    setSelectedRepos(next)
                  }}
                >
                  全选当前列表 (排除白名单)
                </Button>
                {selectedRepos.size > 0 && (
                  <Button
                    variant="ghost"
                    size="sm"
                    className="h-7 text-xs"
                    onClick={() => setSelectedRepos(new Set())}
                  >
                    清空选择
                  </Button>
                )}
              </div>

              <div className="flex flex-wrap items-center gap-2">
                <Button
                  variant="outline"
                  size="sm"
                  className="h-8 text-xs"
                  disabled={selectedRepos.size === 0}
                  onClick={copyGhCliCommands}
                >
                  {copiedCmd ? <Check className="h-3.5 w-3.5" /> : <Copy className="h-3.5 w-3.5" />}
                  <span>复制 gh CLI 批量取关命令</span>
                </Button>

                <Button
                  variant="destructive"
                  size="sm"
                  className="h-8 text-xs"
                  disabled={selectedRepos.size === 0 || unstarBusy === "BATCH"}
                  onClick={handleBatchUnstar}
                >
                  <Trash2 className="h-3.5 w-3.5" />
                  <span>
                    {unstarBusy === "BATCH"
                      ? "正在批量取消 Star..."
                      : ghToken
                      ? `一键批量取消 Star (${selectedRepos.size})`
                      : `配置 Token 后批量取消 Star (${selectedRepos.size})`}
                  </span>
                </Button>
              </div>
            </div>
          )}

          {/* Content Area (Shared across tabs based on filteredRepos) */}
          <div className="mt-4">
            {filteredRepos.length === 0 ? (
              <Card className="p-12 text-center">
                <p className="text-sm text-muted-foreground">没有匹配的仓库，试试调整搜索词或筛选条件。</p>
              </Card>
            ) : viewMode === "grid" ? (
              <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
                {filteredRepos.map((item) => {
                  const isSelected = selectedRepos.has(item.repo)
                  const isKept = keepRepos.has(item.repo)
                  return (
                    <Card
                      key={item.repo}
                      className={`flex flex-col justify-between transition-all hover:shadow-md ${
                        isSelected ? "ring-2 ring-primary" : ""
                      }`}
                    >
                      <div>
                        <CardHeader className="pb-2.5">
                          <div className="flex items-start justify-between gap-2">
                            <div className="flex items-center gap-2.5 min-w-0">
                              <input
                                type="checkbox"
                                checked={isSelected}
                                onChange={() => toggleSelectRepo(item.repo)}
                                className="h-4 w-4 rounded border-input accent-primary cursor-pointer"
                                title="勾选以批量管理"
                              />
                              <img
                                src={item.avatar_url}
                                alt={item.owner}
                                className="h-6 w-6 rounded-full border"
                                loading="lazy"
                              />
                              <a
                                href={item.html_url}
                                target="_blank"
                                rel="noopener noreferrer"
                                className="truncate font-semibold hover:underline"
                                title={item.repo}
                              >
                                {item.repo}
                              </a>
                            </div>
                            <Button
                              variant="ghost"
                              size="icon"
                              className="h-7 w-7 shrink-0"
                              onClick={() => toggleKeepRepo(item.repo)}
                              title={isKept ? "从保留白名单移除" : "加入保留白名单（清理时忽略）"}
                            >
                              <BookmarkCheck
                                className={`h-4 w-4 ${
                                  isKept ? "text-emerald-500" : "text-muted-foreground"
                                }`}
                              />
                            </Button>
                          </div>

                          <div className="flex flex-wrap items-center gap-1.5 pt-1">
                            <Badge variant="secondary" className="text-[11px]">
                              {item.category}
                            </Badge>
                            {item.language && (
                              <Badge variant="outline" className="text-[11px]">
                                💻 {item.language}
                              </Badge>
                            )}
                            {renderStatusBadge(item)}
                          </div>
                        </CardHeader>

                        <CardContent className="space-y-3 pb-3">
                          <p className="line-clamp-2 text-xs leading-relaxed text-muted-foreground">
                            {item.desc_zh || item.description || "暂无项目描述"}
                          </p>

                          {item.release && (
                            <div className="rounded-lg border bg-muted/40 p-2.5 text-xs space-y-1.5">
                              <div className="flex items-center justify-between gap-2">
                                <a
                                  href={item.release.url}
                                  target="_blank"
                                  rel="noopener noreferrer"
                                  className="font-semibold text-blue-600 dark:text-blue-400 hover:underline flex items-center gap-1"
                                >
                                  <Rocket className="h-3.5 w-3.5" />
                                  <span>{item.release.tag}</span>
                                </a>
                                <span className="text-[11px] text-muted-foreground">
                                  {item.release.published_at}
                                </span>
                              </div>
                              <p className="line-clamp-3 whitespace-pre-line text-xs text-foreground/90">
                                {item.release.summary_zh}
                              </p>
                              {item.release.raw_body && (
                                <button
                                  onClick={() => setDetailRepo(item)}
                                  className="inline-flex items-center gap-1 text-[11px] font-medium text-primary hover:underline pt-0.5"
                                >
                                  <FileText className="h-3 w-3" />
                                  查看完整 Release Notes
                                </button>
                              )}
                            </div>
                          )}

                          {item.topics && item.topics.length > 0 && (
                            <div className="flex flex-wrap gap-1">
                              {item.topics.slice(0, 5).map((t) => (
                                <span
                                  key={t}
                                  onClick={() => setSearch(t)}
                                  className="cursor-pointer rounded bg-secondary/70 px-1.5 py-0.5 text-[10px] text-muted-foreground hover:text-foreground"
                                >
                                  #{t}
                                </span>
                              ))}
                            </div>
                          )}
                        </CardContent>
                      </div>

                      <CardFooter className="flex items-center justify-between border-t pt-3 text-xs text-muted-foreground">
                        <div className="flex items-center gap-3">
                          <span className="flex items-center gap-1 font-medium text-foreground">
                            <Star className="h-3.5 w-3.5 text-amber-400 fill-amber-400" />
                            {item.stars.toLocaleString()}
                          </span>
                          <span className="flex items-center gap-1">
                            <GitFork className="h-3.5 w-3.5" />
                            {item.forks.toLocaleString()}
                          </span>
                          <span title="最近代码推送日期">🕒 {item.pushed_at || "未知"}</span>
                        </div>

                        <div className="flex items-center gap-1.5">
                          <Button
                            variant={item.status === "abandoned" ? "destructive" : "outline"}
                            size="sm"
                            className="h-7 px-2.5 text-xs"
                            disabled={unstarBusy === item.repo}
                            onClick={() => handleUnstarSingle(item.repo, item.html_url)}
                          >
                            {unstarBusy === item.repo ? (
                              "处理中..."
                            ) : ghToken ? (
                              <>
                                <Trash2 className="h-3 w-3" />
                                <span>取消 Star</span>
                              </>
                            ) : (
                              <>
                                <ExternalLink className="h-3 w-3" />
                                <span>管理</span>
                              </>
                            )}
                          </Button>
                        </div>
                      </CardFooter>
                    </Card>
                  )
                })}
              </div>
            ) : (
              /* Table View */
              <Card>
                <Table>
                  <TableHeader>
                    <TableRow>
                      <TableHead className="w-10">
                        <input
                          type="checkbox"
                          checked={
                            filteredRepos.length > 0 &&
                            filteredRepos.every((r) => selectedRepos.has(r.repo))
                          }
                          onChange={(e) => {
                            if (e.target.checked) {
                              const next = new Set(selectedRepos)
                              filteredRepos.forEach((r) => next.add(r.repo))
                              setSelectedRepos(next)
                            } else {
                              setSelectedRepos(new Set())
                            }
                          }}
                          className="h-4 w-4 rounded border-input accent-primary cursor-pointer"
                        />
                      </TableHead>
                      <TableHead>仓库名称</TableHead>
                      <TableHead>分类 / 语言</TableHead>
                      <TableHead>Stars</TableHead>
                      <TableHead>健康状态 / 最后提交</TableHead>
                      <TableHead>近期版本</TableHead>
                      <TableHead className="text-right">操作</TableHead>
                    </TableRow>
                  </TableHeader>
                  <TableBody>
                    {filteredRepos.map((item) => {
                      const isSelected = selectedRepos.has(item.repo)
                      const isKept = keepRepos.has(item.repo)
                      return (
                        <TableRow key={item.repo}>
                          <TableCell>
                            <input
                              type="checkbox"
                              checked={isSelected}
                              onChange={() => toggleSelectRepo(item.repo)}
                              className="h-4 w-4 rounded border-input accent-primary cursor-pointer"
                            />
                          </TableCell>
                          <TableCell className="max-w-[260px]">
                            <div className="flex items-center gap-2">
                              <img
                                src={item.avatar_url}
                                alt={item.owner}
                                className="h-5 w-5 rounded-full"
                                loading="lazy"
                              />
                              <a
                                href={item.html_url}
                                target="_blank"
                                rel="noopener noreferrer"
                                className="font-medium hover:underline truncate"
                              >
                                {item.repo}
                              </a>
                            </div>
                            <p className="truncate text-xs text-muted-foreground mt-0.5">
                              {item.desc_zh || item.description}
                            </p>
                          </TableCell>
                          <TableCell>
                            <div className="flex flex-col gap-1">
                              <span className="text-xs">{item.category}</span>
                              <span className="text-[11px] text-muted-foreground">
                                {item.language || "Other"}
                              </span>
                            </div>
                          </TableCell>
                          <TableCell className="font-medium">
                            ⭐ {item.stars.toLocaleString()}
                          </TableCell>
                          <TableCell>
                            <div className="flex flex-col gap-1">
                              <div>{renderStatusBadge(item)}</div>
                              <span className="text-[11px] text-muted-foreground">
                                最后推送: {item.pushed_at}
                              </span>
                            </div>
                          </TableCell>
                          <TableCell>
                            {item.release ? (
                              <button
                                onClick={() => setDetailRepo(item)}
                                className="text-left text-xs text-blue-500 hover:underline"
                              >
                                <div className="font-semibold">{item.release.tag}</div>
                                <div className="text-[11px] text-muted-foreground">
                                  {item.release.published_at}
                                </div>
                              </button>
                            ) : (
                              <span className="text-xs text-muted-foreground">-</span>
                            )}
                          </TableCell>
                          <TableCell className="text-right">
                            <div className="flex items-center justify-end gap-1.5">
                              <Button
                                variant="ghost"
                                size="icon"
                                className="h-7 w-7"
                                onClick={() => toggleKeepRepo(item.repo)}
                                title={isKept ? "取消白名单保留" : "加入白名单保留"}
                              >
                                <BookmarkCheck
                                  className={`h-4 w-4 ${
                                    isKept ? "text-emerald-500" : "text-muted-foreground"
                                  }`}
                                />
                              </Button>
                              <Button
                                variant={item.status === "abandoned" ? "destructive" : "outline"}
                                size="sm"
                                className="h-7 px-2.5 text-xs"
                                onClick={() => handleUnstarSingle(item.repo, item.html_url)}
                              >
                                {ghToken ? "取消 Star" : "前往仓库"}
                              </Button>
                            </div>
                          </TableCell>
                        </TableRow>
                      )
                    })}
                  </TableBody>
                </Table>
              </Card>
            )}
          </div>
        </Tabs>
      </main>

      {/* Release Notes Modal */}
      <Dialog open={!!detailRepo} onOpenChange={(open) => !open && setDetailRepo(null)}>
        <DialogContent>
          {detailRepo && (
            <>
              <DialogHeader>
                <DialogTitle className="flex items-center gap-2">
                  <span>📦 {detailRepo.repo}</span>
                  {detailRepo.release && (
                    <Badge variant="secondary">{detailRepo.release.tag}</Badge>
                  )}
                </DialogTitle>
                <DialogDescription>
                  发布时间：{detailRepo.release?.published_at} · ⭐{" "}
                  {detailRepo.stars.toLocaleString()} Stars
                </DialogDescription>
              </DialogHeader>

              <div className="space-y-4 text-sm">
                <div className="rounded-lg border bg-muted/40 p-3.5 space-y-1.5">
                  <div className="font-semibold text-xs text-primary">
                    💡 核心亮点更新 (中文提炼)
                  </div>
                  <p className="whitespace-pre-line text-xs leading-relaxed">
                    {detailRepo.release?.summary_zh}
                  </p>
                </div>

                {detailRepo.release?.raw_body && (
                  <div className="space-y-1.5">
                    <div className="font-semibold text-xs text-muted-foreground">
                      🔍 官方原版 Release Notes
                    </div>
                    <pre className="max-h-72 overflow-auto rounded-lg border bg-muted/50 p-3 text-xs whitespace-pre-wrap font-mono">
                      {detailRepo.release.raw_body}
                    </pre>
                  </div>
                )}

                <div className="flex justify-end gap-2 pt-2">
                  {detailRepo.release?.url && (
                    <Button variant="outline" size="sm" asChild>
                      <a
                        href={detailRepo.release.url}
                        target="_blank"
                        rel="noopener noreferrer"
                      >
                        <ExternalLink className="h-3.5 w-3.5" />
                        查看 GitHub Release
                      </a>
                    </Button>
                  )}
                  <Button size="sm" asChild>
                    <a
                      href={detailRepo.html_url}
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      <Github className="h-3.5 w-3.5" />
                      访问项目主页
                    </a>
                  </Button>
                </div>
              </div>
            </>
          )}
        </DialogContent>
      </Dialog>

      {/* GitHub Token Modal */}
      <Dialog open={tokenModalOpen} onOpenChange={setTokenModalOpen}>
        <DialogContent>
          <DialogHeader>
            <DialogTitle className="flex items-center gap-2">
              <KeyRound className="h-5 w-5 text-primary" />
              <span>连接 GitHub Token（支持在看板直接取消 Star）</span>
            </DialogTitle>
            <DialogDescription>
              Token 仅保存在您当前浏览器的 <code>localStorage</code> 中，绝不会上传至任何服务器。
            </DialogDescription>
          </DialogHeader>

          <div className="space-y-4 text-sm">
            <div className="rounded-lg border bg-muted/40 p-3 text-xs space-y-1 text-muted-foreground">
              <p>1. 前往 GitHub Settings → Developer settings → Personal access tokens (Classic)</p>
              <p>
                2. 生成 Token 时勾选 <code>public_repo</code>（或 <code>user</code>）权限即可用于管理 Star。
              </p>
              <p>3. 配置后，点击看板中的「取消 Star」或「一键批量取消 Star」将直接调用 GitHub API 生效。</p>
            </div>

            <div className="space-y-2">
              <label className="text-xs font-medium">Personal Access Token (ghp_...)</label>
              <Input
                type="password"
                placeholder="粘贴您的 GitHub Token..."
                value={tokenInput}
                onChange={(e) => setTokenInput(e.target.value)}
              />
            </div>

            <div className="flex justify-end gap-2">
              {ghToken && (
                <Button
                  variant="outline"
                  size="sm"
                  onClick={() => {
                    setTokenInput("")
                    setGhToken("")
                    localStorage.removeItem(STORAGE_TOKEN_KEY)
                    setTokenModalOpen(false)
                    showToast("已清除本地 Token")
                  }}
                >
                  清除已存 Token
                </Button>
              )}
              <Button variant="outline" size="sm" onClick={() => setTokenModalOpen(false)}>
                取消
              </Button>
              <Button size="sm" onClick={saveToken}>
                保存配置
              </Button>
            </div>
          </div>
        </DialogContent>
      </Dialog>
    </div>
  )
}
